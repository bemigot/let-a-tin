# acme-dns-tiny

Based on [acme-dns-tiny](https://gitlab.adorsaz.ch/adrien/acme-dns-tiny/) also [on Github](https://github.com/Trim/acme-dns-tiny), [acme-tiny](https://github.com/diafygi/acme-tiny).


This is a tiny, auditable script that you can throw on any secure machine to issue
and renew [Let's Encrypt](https://letsencrypt.org/) certificates with DNS validation.

Using ACME [RFC 8555](https://tools.ietf.org/html/rfc8555) DNS challenge you may
* create wildcard certificates
* issue certificates for servers not exposed on Internet, e.g. *development machines*
* run this script on machine not exposed on Internet

Since this script has to read your private ACME account key and must have the
rights to update the DNS records of your authoritative DNS server, this code has been designed
to be as tiny as possible (currently around 400 lines).

**READ THE SOURCE CODE! YOU MUST TRUST IT**

Prerequisites: Python 3.9+, the `openssl` command and the `dnspython` module (at least 2.0).

## Donate

If this script is useful to you, please donate to the EFF. I don't work there,
but they do fantastic work.

[https://eff.org/donate/](https://eff.org/donate/)

## How to use this script

See the [HowTo Use](./howto-use.md).

Note that, this script can be run on any secure machine which have access to
Internet and your public DNS server.

## Permissions

The biggest problem you'll likely come across while setting up and running this
script is permissions.

You want to limit access for this script to:
* Your account private key
* Your Certificate Signing Request (CSR) file (without your private domain key)
* Your configuration file (which contains the secret to do dynamic DNS updates)

I'd recommend to create a user specifically to run this script and the
above files. This user should *NOT* have access to your private domain key!

**BE SURE TO:**
* Backup your account private key (e.g. `account.key`)
* Don't run this script as *root*
* Don't let this script read your *domain* private key
* Understand and configure correctly your cron jobs
