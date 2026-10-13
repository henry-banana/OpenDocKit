from pathlib import Path
import tempfile
import unittest

from tools.validate_contracts import validate_contracts


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.folder = self.root / "templates/comprehensive/contracts"
        self.folder.mkdir(parents=True)

    def check(self, name, content):
        (self.folder / name).write_text(content, encoding="utf-8")
        return {
            i.code
            for i in validate_contracts(
                self.root,
                [
                    {"path": p.relative_to(self.root).as_posix(), "kind": "contract"}
                    for p in self.folder.iterdir()
                ],
            )
        }

    def test_sibling_root_real_name_contract(self):
        path = self.root / "templates-service/minimal/contracts/openapi.yaml"
        path.parent.mkdir(parents=True)
        path.write_text("openapi: [broken", encoding="utf-8")
        self.assertIn(
            "CONTRACT_PARSE",
            {
                i.code
                for i in validate_contracts(
                    self.root,
                    [
                        {
                            "path": path.relative_to(self.root).as_posix(),
                            "kind": "contract",
                        }
                    ],
                )
            },
        )

    def test_missing_registered_contract(self):
        self.assertIn(
            "MISSING_TEMPLATE",
            {
                i.code
                for i in validate_contracts(
                    self.root,
                    [
                        {
                            "path": "templates/minimal/contracts/openapi.yaml",
                            "kind": "contract",
                        }
                    ],
                )
            },
        )

    def test_malformed_json(self):
        self.assertIn("CONTRACT_PARSE", self.check("json-schema.json", "{bad"))

    def test_invalid_schema(self):
        self.assertIn(
            "CONTRACT_SCHEMA", self.check("json-schema.json", '{"type":"not-a-type"}')
        )

    def test_invalid_yaml(self):
        self.assertIn("CONTRACT_PARSE", self.check("openapi.yaml", "openapi: [broken"))

    def test_wrong_openapi_version(self):
        self.assertIn(
            "CONTRACT_SCHEMA",
            self.check(
                "openapi.yaml",
                'openapi: 7.0.0\ninfo: {title: Test, version: "1"}\npaths: {}',
            ),
        )

    def test_wrong_asyncapi_version(self):
        self.assertIn(
            "CONTRACT_SCHEMA",
            self.check(
                "asyncapi.yaml",
                'asyncapi: 0.1.0\ninfo: {title: Test, version: "1"}\nchannels: {}',
            ),
        )

    def test_asyncapi_missing_version(self):
        self.assertIn(
            "CONTRACT_SCHEMA",
            self.check(
                "asyncapi.yaml",
                "asyncapi: 3.0.0\ninfo: {title: Test}\nchannels: {}\noperations: {}",
            ),
        )

    def test_unknown_asyncapi_extension_requires_external_validation(self):
        self.assertIn(
            "CONTRACT_SCHEMA",
            self.check(
                "asyncapi.yaml",
                'asyncapi: 3.0.0\ninfo: {title: Test, version: "1"}\nchannels: {invented: {}}\noperations: {}',
            ),
        )

    def test_invalid_graphql_syntax(self):
        self.assertIn(
            "CONTRACT_SCHEMA", self.check("graphql.graphql", "type Query { broken: }")
        )

    def test_invalid_graphql_type(self):
        self.assertIn(
            "CONTRACT_SCHEMA",
            self.check("graphql.graphql", "type Query { value: UnknownType }"),
        )

    def test_invalid_proto(self):
        self.assertIn(
            "CONTRACT_SCHEMA",
            self.check("protobuf.proto", 'syntax = "proto3"; message { bad }'),
        )

    def test_duplicate_yaml_keys_are_rejected(self):
        self.assertIn(
            "CONTRACT_PARSE",
            self.check(
                "openapi.yaml",
                'openapi: 3.1.0\nopenapi: 3.1.0\ninfo: {title: Test, version: "1"}\npaths: {}',
            ),
        )

    def test_external_reference_is_not_fetched(self):
        self.assertIn(
            "CONTRACT_SCHEMA",
            self.check(
                "openapi.yaml",
                'openapi: 3.1.0\ninfo: {title: Test, version: "1"}\npaths: {}\ncomponents:\n  schemas:\n    External:\n      $ref: https://example.invalid/no-fetch',
            ),
        )

    def test_valid_minimal_contracts(self):
        sources = {
            "openapi.yaml": 'openapi: 3.1.0\ninfo: {title: Test, version: "1"}\npaths: {}',
            "asyncapi.yaml": 'asyncapi: 3.0.0\ninfo: {title: Test, version: "1"}\nchannels: {}\noperations: {}',
            "json-schema.json": '{"$schema":"https://json-schema.org/draft/2020-12/schema","type":"object"}',
            "graphql.graphql": "type Query { value: String }",
            "protobuf.proto": 'syntax = "proto3"; message Example {}',
        }
        for name, content in sources.items():
            (self.folder / name).write_text(content, encoding="utf-8")
        self.assertEqual(
            validate_contracts(
                self.root,
                [
                    {"path": p.relative_to(self.root).as_posix(), "kind": "contract"}
                    for p in self.folder.iterdir()
                ],
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()
