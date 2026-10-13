# Security Policy

## Scope and supported material

This policy covers OpenDocKit's documentation, template/configuration samples
and maintainer tooling. Report unsafe instructions that could cause harm,
sensitive information exposed in source, unexpected executable behavior or a
vulnerability in the validation tools/dependencies.

Fixes are maintained in the current development tree. Older copied templates do
not receive automatic updates, and no backport schedule is promised. Include the
commit or version you used so maintainers can assess whether it is affected.
Adopting teams remain responsible for their applications and selected agent
configuration.

## Report a vulnerability

**Share sensitive details through a private route, not a public issue or PR.**

1. Open the repository's [Security area](https://github.com/henry-banana/OpenDocKit/security).
   If **Report a vulnerability** is available, use GitHub's private reporting
   flow.
2. If private reporting is unavailable, open an
   [issue requesting a private contact route](https://github.com/henry-banana/OpenDocKit/issues/new).
   Include no exploit details, credentials, private data or affected people's
   identities. Wait until a maintainer establishes that route before sharing
   the report.

The presence of this policy does not establish that private reporting has been
enabled on GitHub. Ordinary broken links or documentation questions can use the
public routes in [SUPPORT.md](SUPPORT.md).

## What to include privately

- Affected files, source commit/version and relevant runtime/client versions.
- The suspected impact and conditions needed to trigger it.
- A minimal reproduction with sanitized input/output or other safe evidence.
- Any mitigation you know and your preference for attribution.

Use only systems and data you are authorized to test. Remove credentials and
unnecessary personal or customer data from the evidence.

## Handling and disclosure

Maintainers investigate reports, discuss fixes and mitigations, and coordinate
public disclosure with the reporter where possible. When a fix affects copied
templates, describe the changes an adopting team needs to make; the library
cannot update those copies itself.

This is a community-maintained project with no guaranteed response timeline.
Static validation checks do not establish the security of an adopted application
or certify a client configuration.
