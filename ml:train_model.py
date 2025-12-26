Last login: Wed Dec 24 16:00:08 on ttys002
mohammedtawheed@Mohammeds-MacBook-Pro-2 mitre-soc-simulator % mkdir phishing-url-detector
cd phishing-url-detector

mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % mkdir data src reports
touch README.md requirements.txt .gitignore
touch data/sample_urls.txt
touch src/main.py src/url_analyzer.py src/rules.py src/report_generator.py

mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 --version

Python 3.9.6
mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % Python 3.9+ 

zsh: command not found: Python
mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 --version

Python 3.9.6
mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 -m venv venv
source venv/bin/activate

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/rules.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/url_analyzer.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano data/sample_urls.txt

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/report_generator.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % cat reports/phishing_report.txt

cat: reports/phishing_report.txt: No such file or directory
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % cat reports/phishing_report.txt

cat: reports/phishing_report.txt: No such file or directory
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % pwd
/Users/mohammedtawheed/mitre-soc-simulator/phishing-url-detector
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % cd src
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % cd src

cd: no such file or directory: src
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano ../data/sample_urls.txt

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 8
    with open(DATA_FILE, "r") as file:
    ^
IndentationError: expected an indented block
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

Traceback (most recent call last):
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 3, in <module>
    from report_generator import generate_report
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/report_generator.py", line 1
    [PHISHING] http://192.168.1.10/login (Score: 6)
               ^
SyntaxError: invalid syntax
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano report_generator.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

DEBUG: URLs read from file → ['http://192.168.1.10/login\n', 'https://secure-paypal.com.verify.account-update.ru\n', 'https://google.com\n', 'http://free-gift-login.com\n', '\n']
[SUSPICIOUS] http://192.168.1.10/login (Score: 5)
[SUSPICIOUS] https://secure-paypal.com.verify.account-update.ru (Score: 3)
[SAFE] https://google.com (Score: 0)
[SUSPICIOUS] http://free-gift-login.com (Score: 3)

Report saved to reports/phishing_report.txt
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 20
    urls = file.readlines())
                           ^
SyntaxError: unmatched ')'
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % nano main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % python3 main.py

[SUSPICIOUS] http://192.168.1.10/login (Score: 5)
[SUSPICIOUS] https://secure-paypal.com.verify.account-update.ru (Score: 3)
[SAFE] https://google.com (Score: 0)
[SUSPICIOUS] http://free-gift-login.com (Score: 3)

Report saved to reports/phishing_report.txt
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 src % cd ..
cat reports/phishing_report.txt

PHISHING URL DETECTION REPORT
===================================
Generated on: 2025-12-24 19:32:29.493294

URL: http://192.168.1.10/login
Risk Score: 5
Status: SUSPICIOUS
Reasons:
- Uses IP address instead of domain
- Uses HTTP instead of HTTPS
- Contains phishing keywords
-----------------------------------
URL: https://secure-paypal.com.verify.account-update.ru
Risk Score: 3
Status: SUSPICIOUS
Reasons:
- Too many subdomains
- Contains phishing keywords
-----------------------------------
URL: https://google.com
Risk Score: 0
Status: SAFE
Reasons: None
-----------------------------------
URL: http://free-gift-login.com
Risk Score: 3
Status: SUSPICIOUS
Reasons:
- Uses HTTP instead of HTTPS
- Contains phishing keywords
-----------------------------------
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % cd ~/Documents/phishing-url-detector

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git init

Initialized empty Git repository in /Users/mohammedtawheed/Documents/phishing-url-detector/.git/
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git add .

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git commit -m "Initial commit: Phishing URL Detection Tool"

[main (root-commit) a2f6d88] Initial commit: Phishing URL Detection Tool
 587 files changed, 210661 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 data/sample_urls.txt
 create mode 100644 data:sample_urls.txt
 create mode 100644 python3 main.py
 create mode 100644 report_generator.py
 create mode 100644 reports/phishing_report.txt
 create mode 100644 requirements.txt
 create mode 100644 src/main.py
 create mode 100644 src/report_generator.py
 create mode 100644 src/rules.py
 create mode 100644 src/url_analyzer.py
 create mode 100644 src:main.py
 create mode 100644 src:rules.py
 create mode 100644 src:url_analyzer.py
 create mode 100644 venv/bin/Activate.ps1
 create mode 100644 venv/bin/activate
 create mode 100644 venv/bin/activate.csh
 create mode 100644 venv/bin/activate.fish
 create mode 100755 venv/bin/pip
 create mode 100755 venv/bin/pip3
 create mode 100755 venv/bin/pip3.9
 create mode 120000 venv/bin/python
 create mode 120000 venv/bin/python3
 create mode 120000 venv/bin/python3.9
 create mode 100644 venv/lib/python3.9/site-packages/_distutils_hack/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/_distutils_hack/override.py
 create mode 100644 venv/lib/python3.9/site-packages/distutils-precedence.pth
 create mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/INSTALLER
 create mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/LICENSE.txt
 create mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/METADATA
 create mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/RECORD
 create mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/REQUESTED
 create mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/WHEEL
 create mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/entry_points.txt
 create mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/top_level.txt
 create mode 100644 venv/lib/python3.9/site-packages/pip/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/__main__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/build_env.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cache.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/autocompletion.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/base_command.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/cmdoptions.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/command_context.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/main.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/main_parser.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/parser.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/progress_bars.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/req_command.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/spinners.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/status_codes.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/cache.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/check.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/completion.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/configuration.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/debug.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/download.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/freeze.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/hash.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/help.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/index.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/install.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/list.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/search.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/show.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/uninstall.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/wheel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/configuration.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/distributions/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/distributions/base.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/distributions/installed.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/distributions/sdist.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/distributions/wheel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/exceptions.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/index/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/index/collector.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/index/package_finder.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/index/sources.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/locations/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/locations/_distutils.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/locations/_sysconfig.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/locations/base.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/main.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/metadata/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/metadata/base.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/metadata/pkg_resources.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/candidate.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/direct_url.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/format_control.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/index.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/link.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/scheme.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/search_scope.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/selection_prefs.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/target_python.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/wheel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/auth.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/cache.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/download.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/lazy_wheel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/session.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/utils.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/xmlrpc.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/build/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/build/metadata.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/build/metadata_legacy.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/build/wheel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/build/wheel_legacy.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/check.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/freeze.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/install/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/install/editable_legacy.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/install/legacy.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/install/wheel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/prepare.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/pyproject.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/constructors.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/req_file.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/req_install.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/req_set.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/req_tracker.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/req_uninstall.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/base.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/legacy/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/legacy/resolver.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/base.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/factory.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/provider.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/reporter.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/requirements.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/resolver.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/self_outdated_check.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/_log.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/appdirs.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/compat.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/compatibility_tags.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/datetime.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/deprecation.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/direct_url_helpers.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/distutils_args.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/encoding.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/entrypoints.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/filesystem.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/filetypes.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/glibc.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/hashes.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/inject_securetransport.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/logging.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/misc.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/models.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/packaging.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/parallel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/pkg_resources.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/setuptools_build.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/subprocess.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/temp_dir.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/unpacking.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/urls.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/virtualenv.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/wheel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/vcs/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/vcs/bazaar.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/vcs/git.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/vcs/mercurial.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/vcs/subversion.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/vcs/versioncontrol.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_internal/wheel_builder.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/appdirs.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/_cmd.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/adapter.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/cache.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/file_cache.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/redis_cache.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/compat.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/controller.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/filewrapper.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/heuristics.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/serialize.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/wrapper.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/certifi/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/certifi/__main__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/certifi/cacert.pem
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/certifi/core.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/big5freq.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/big5prober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/chardistribution.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/charsetgroupprober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/charsetprober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/cli/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/cli/chardetect.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/codingstatemachine.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/compat.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/cp949prober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/enums.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/escprober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/escsm.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/eucjpprober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/euckrfreq.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/euckrprober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/euctwfreq.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/euctwprober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/gb2312freq.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/gb2312prober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/hebrewprober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/jisfreq.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/jpcntx.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langbulgarianmodel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langgreekmodel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langhebrewmodel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langhungarianmodel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langrussianmodel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langthaimodel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langturkishmodel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/latin1prober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcharsetprober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcsgroupprober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcssm.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/metadata/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/metadata/languages.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/sbcharsetprober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/sbcsgroupprober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/sjisprober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/universaldetector.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/utf8prober.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/version.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/colorama/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/colorama/ansi.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/colorama/ansitowin32.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/colorama/initialise.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/colorama/win32.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/colorama/winterm.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/misc.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/shutil.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/sysconfig.cfg
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/sysconfig.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/tarfile.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/compat.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/database.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/index.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/locators.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/manifest.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/markers.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/metadata.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/resources.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/scripts.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/t32.exe
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/t64.exe
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/util.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/version.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/w32.exe
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/w64.exe
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/wheel.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distro.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_ihatexml.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_inputstream.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_tokenizer.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/_base.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/py.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_utils.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/constants.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/alphabeticalattributes.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/base.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/inject_meta_charset.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/lint.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/optionaltags.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/sanitizer.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/whitespace.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/html5parser.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/serializer.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/genshi.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/sax.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/base.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/dom.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/etree.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/etree_lxml.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/base.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/dom.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/etree.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/etree_lxml.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/genshi.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/codec.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/compat.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/core.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/idnadata.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/intranges.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/package_data.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/uts46data.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/msgpack/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/msgpack/_version.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/msgpack/exceptions.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/msgpack/ext.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/msgpack/fallback.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/__about__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/_manylinux.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/_musllinux.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/_structures.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/markers.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/requirements.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/specifiers.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/tags.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/utils.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/version.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/build.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/check.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/colorlog.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/compat.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/dirtools.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/envbuild.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/_in_process.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/meta.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/wrappers.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pkg_resources/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pkg_resources/py31compat.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/progress/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/progress/bar.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/progress/counter.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/progress/spinner.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pyparsing.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/__version__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/_internal_utils.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/adapters.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/api.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/auth.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/certs.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/compat.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/cookies.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/exceptions.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/help.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/hooks.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/models.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/packages.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/sessions.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/status_codes.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/structures.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/utils.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/compat/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/compat/collections_abc.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/providers.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/reporters.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/structs.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/six.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/_asyncio.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/_utils.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/after.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/before.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/before_sleep.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/nap.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/retry.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/stop.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/tornadoweb.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/wait.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tomli/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tomli/_parser.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tomli/_re.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/_collections.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/_version.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/connection.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/connectionpool.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_appengine_environ.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/bindings.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/low_level.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/appengine.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/ntlmpool.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/pyopenssl.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/securetransport.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/socks.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/exceptions.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/fields.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/filepost.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/backports/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/backports/makefile.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/six.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/ssl_match_hostname/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/ssl_match_hostname/_implementation.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/poolmanager.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/request.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/connection.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/proxy.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/queue.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/request.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/response.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/retry.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/ssl_.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/ssltransport.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/timeout.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/url.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/wait.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/vendor.txt
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/webencodings/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/webencodings/labels.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/webencodings/mklabels.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/webencodings/tests.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/webencodings/x_user_defined.py
 create mode 100644 venv/lib/python3.9/site-packages/pip/py.typed
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/appdirs.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/__about__.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_compat.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_structures.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_typing.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/markers.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/requirements.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/specifiers.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/tags.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/utils.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/version.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/pyparsing.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/extern/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/pkg_resources/tests/data/my-test-package-source/setup.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/INSTALLER
 create mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/LICENSE
 create mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/METADATA
 create mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/RECORD
 create mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/REQUESTED
 create mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/WHEEL
 create mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/entry_points.txt
 create mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/top_level.txt
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_deprecation_warning.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/_msvccompiler.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/archive_util.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/bcppcompiler.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/ccompiler.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/cmd.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_dumb.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_msi.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_rpm.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_wininst.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/build.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_clib.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_ext.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_py.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_scripts.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/check.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/clean.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/config.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/install.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_data.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_egg_info.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_headers.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_lib.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_scripts.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/py37compat.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/register.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/sdist.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/upload.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/config.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/core.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/cygwinccompiler.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/debug.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/dep_util.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/dir_util.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/dist.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/errors.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/extension.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/fancy_getopt.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/file_util.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/filelist.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/log.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/msvc9compiler.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/msvccompiler.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/py35compat.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/py38compat.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/spawn.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/sysconfig.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/text_file.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/unixccompiler.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/util.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/version.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/versionpredicate.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_imp.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/more.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/recipes.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/ordered_set.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/__about__.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_compat.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_structures.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_typing.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/markers.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/requirements.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/specifiers.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/tags.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/utils.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/version.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/pyparsing.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/archive_util.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/build_meta.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/cli-32.exe
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/cli-64.exe
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/cli.exe
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/alias.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/bdist_egg.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/bdist_rpm.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/build_clib.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/build_ext.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/build_py.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/develop.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/dist_info.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/easy_install.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/egg_info.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/install.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/install_egg_info.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/install_lib.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/install_scripts.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/launcher manifest.xml
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/py36compat.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/register.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/rotate.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/saveopts.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/sdist.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/setopt.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/test.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/upload.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/command/upload_docs.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/config.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/dep_util.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/depends.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/dist.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/errors.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/extension.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/extern/__init__.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/glob.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/gui-32.exe
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/gui-64.exe
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/gui.exe
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/installer.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/launch.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/monkey.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/msvc.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/namespaces.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/package_index.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/py34compat.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/sandbox.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/script (dev).tmpl
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/script.tmpl
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/unicode_utils.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/version.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/wheel.py
 create mode 100644 venv/lib/python3.9/site-packages/setuptools/windows_support.py
 create mode 100644 venv/pyvenv.cfg
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano .gitignore

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git rm -r --cached venv

rm 'venv/bin/Activate.ps1'
rm 'venv/bin/activate'
rm 'venv/bin/activate.csh'
rm 'venv/bin/activate.fish'
rm 'venv/bin/pip'
rm 'venv/bin/pip3'
rm 'venv/bin/pip3.9'
rm 'venv/bin/python'
rm 'venv/bin/python3'
rm 'venv/bin/python3.9'
rm 'venv/lib/python3.9/site-packages/_distutils_hack/__init__.py'
rm 'venv/lib/python3.9/site-packages/_distutils_hack/override.py'
rm 'venv/lib/python3.9/site-packages/distutils-precedence.pth'
rm 'venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/INSTALLER'
rm 'venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/LICENSE.txt'
rm 'venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/METADATA'
rm 'venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/RECORD'
rm 'venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/REQUESTED'
rm 'venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/WHEEL'
rm 'venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/entry_points.txt'
rm 'venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/top_level.txt'
rm 'venv/lib/python3.9/site-packages/pip/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/__main__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/build_env.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cache.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cli/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cli/autocompletion.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cli/base_command.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cli/cmdoptions.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cli/command_context.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cli/main.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cli/main_parser.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cli/parser.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cli/progress_bars.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cli/req_command.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cli/spinners.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/cli/status_codes.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/cache.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/check.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/completion.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/configuration.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/debug.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/download.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/freeze.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/hash.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/help.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/index.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/install.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/list.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/search.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/show.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/uninstall.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/commands/wheel.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/configuration.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/distributions/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/distributions/base.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/distributions/installed.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/distributions/sdist.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/distributions/wheel.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/exceptions.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/index/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/index/collector.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/index/package_finder.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/index/sources.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/locations/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/locations/_distutils.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/locations/_sysconfig.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/locations/base.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/main.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/metadata/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/metadata/base.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/metadata/pkg_resources.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/models/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/models/candidate.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/models/direct_url.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/models/format_control.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/models/index.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/models/link.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/models/scheme.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/models/search_scope.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/models/selection_prefs.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/models/target_python.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/models/wheel.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/network/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/network/auth.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/network/cache.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/network/download.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/network/lazy_wheel.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/network/session.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/network/utils.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/network/xmlrpc.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/build/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/build/metadata.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/build/metadata_legacy.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/build/wheel.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/build/wheel_legacy.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/check.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/freeze.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/install/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/install/editable_legacy.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/install/legacy.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/install/wheel.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/operations/prepare.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/pyproject.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/req/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/req/constructors.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/req/req_file.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/req/req_install.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/req/req_set.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/req/req_tracker.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/req/req_uninstall.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/base.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/legacy/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/legacy/resolver.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/base.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/factory.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/provider.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/reporter.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/requirements.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/resolver.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/self_outdated_check.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/_log.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/appdirs.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/compat.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/compatibility_tags.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/datetime.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/deprecation.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/direct_url_helpers.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/distutils_args.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/encoding.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/entrypoints.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/filesystem.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/filetypes.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/glibc.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/hashes.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/inject_securetransport.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/logging.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/misc.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/models.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/packaging.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/parallel.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/pkg_resources.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/setuptools_build.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/subprocess.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/temp_dir.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/unpacking.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/urls.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/virtualenv.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/utils/wheel.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/vcs/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/vcs/bazaar.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/vcs/git.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/vcs/mercurial.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/vcs/subversion.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/vcs/versioncontrol.py'
rm 'venv/lib/python3.9/site-packages/pip/_internal/wheel_builder.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/appdirs.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/_cmd.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/adapter.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/cache.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/file_cache.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/redis_cache.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/compat.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/controller.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/filewrapper.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/heuristics.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/serialize.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/wrapper.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/certifi/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/certifi/__main__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/certifi/cacert.pem'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/certifi/core.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/big5freq.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/big5prober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/chardistribution.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/charsetgroupprober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/charsetprober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/cli/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/cli/chardetect.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/codingstatemachine.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/compat.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/cp949prober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/enums.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/escprober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/escsm.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/eucjpprober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/euckrfreq.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/euckrprober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/euctwfreq.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/euctwprober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/gb2312freq.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/gb2312prober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/hebrewprober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/jisfreq.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/jpcntx.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/langbulgarianmodel.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/langgreekmodel.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/langhebrewmodel.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/langhungarianmodel.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/langrussianmodel.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/langthaimodel.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/langturkishmodel.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/latin1prober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcharsetprober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcsgroupprober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcssm.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/metadata/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/metadata/languages.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/sbcharsetprober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/sbcsgroupprober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/sjisprober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/universaldetector.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/utf8prober.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/chardet/version.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/colorama/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/colorama/ansi.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/colorama/ansitowin32.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/colorama/initialise.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/colorama/win32.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/colorama/winterm.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/misc.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/shutil.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/sysconfig.cfg'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/sysconfig.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/tarfile.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/compat.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/database.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/index.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/locators.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/manifest.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/markers.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/metadata.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/resources.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/scripts.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/t32.exe'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/t64.exe'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/util.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/version.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/w32.exe'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/w64.exe'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distlib/wheel.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/distro.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_ihatexml.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_inputstream.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_tokenizer.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/_base.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/py.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_utils.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/constants.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/alphabeticalattributes.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/base.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/inject_meta_charset.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/lint.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/optionaltags.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/sanitizer.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/whitespace.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/html5parser.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/serializer.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/genshi.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/sax.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/base.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/dom.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/etree.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/etree_lxml.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/base.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/dom.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/etree.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/etree_lxml.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/genshi.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/idna/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/idna/codec.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/idna/compat.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/idna/core.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/idna/idnadata.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/idna/intranges.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/idna/package_data.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/idna/uts46data.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/msgpack/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/msgpack/_version.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/msgpack/exceptions.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/msgpack/ext.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/msgpack/fallback.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/packaging/__about__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/packaging/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/packaging/_manylinux.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/packaging/_musllinux.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/packaging/_structures.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/packaging/markers.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/packaging/requirements.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/packaging/specifiers.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/packaging/tags.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/packaging/utils.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/packaging/version.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pep517/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pep517/build.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pep517/check.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pep517/colorlog.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pep517/compat.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pep517/dirtools.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pep517/envbuild.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/_in_process.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pep517/meta.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pep517/wrappers.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pkg_resources/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pkg_resources/py31compat.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/progress/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/progress/bar.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/progress/counter.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/progress/spinner.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/pyparsing.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/__version__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/_internal_utils.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/adapters.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/api.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/auth.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/certs.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/compat.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/cookies.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/exceptions.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/help.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/hooks.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/models.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/packages.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/sessions.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/status_codes.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/structures.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/requests/utils.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/compat/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/compat/collections_abc.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/providers.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/reporters.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/structs.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/six.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tenacity/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tenacity/_asyncio.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tenacity/_utils.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tenacity/after.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tenacity/before.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tenacity/before_sleep.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tenacity/nap.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tenacity/retry.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tenacity/stop.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tenacity/tornadoweb.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tenacity/wait.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tomli/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tomli/_parser.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/tomli/_re.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/_collections.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/_version.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/connection.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/connectionpool.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_appengine_environ.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/bindings.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/low_level.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/appengine.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/ntlmpool.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/pyopenssl.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/securetransport.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/socks.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/exceptions.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/fields.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/filepost.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/backports/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/backports/makefile.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/six.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/ssl_match_hostname/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/ssl_match_hostname/_implementation.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/poolmanager.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/request.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/connection.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/proxy.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/queue.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/request.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/response.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/retry.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/ssl_.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/ssltransport.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/timeout.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/url.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/wait.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/vendor.txt'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/webencodings/__init__.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/webencodings/labels.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/webencodings/mklabels.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/webencodings/tests.py'
rm 'venv/lib/python3.9/site-packages/pip/_vendor/webencodings/x_user_defined.py'
rm 'venv/lib/python3.9/site-packages/pip/py.typed'
rm 'venv/lib/python3.9/site-packages/pkg_resources/__init__.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/__init__.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/appdirs.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/__about__.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/__init__.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_compat.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_structures.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_typing.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/markers.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/requirements.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/specifiers.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/tags.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/utils.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/version.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/_vendor/pyparsing.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/extern/__init__.py'
rm 'venv/lib/python3.9/site-packages/pkg_resources/tests/data/my-test-package-source/setup.py'
rm 'venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/INSTALLER'
rm 'venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/LICENSE'
rm 'venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/METADATA'
rm 'venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/RECORD'
rm 'venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/REQUESTED'
rm 'venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/WHEEL'
rm 'venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/entry_points.txt'
rm 'venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/top_level.txt'
rm 'venv/lib/python3.9/site-packages/setuptools/__init__.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_deprecation_warning.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/__init__.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/_msvccompiler.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/archive_util.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/bcppcompiler.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/ccompiler.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/cmd.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/__init__.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_dumb.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_msi.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_rpm.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_wininst.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/build.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_clib.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_ext.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_py.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_scripts.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/check.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/clean.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/config.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/install.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_data.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_egg_info.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_headers.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_lib.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_scripts.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/py37compat.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/register.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/sdist.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/command/upload.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/config.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/core.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/cygwinccompiler.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/debug.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/dep_util.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/dir_util.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/dist.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/errors.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/extension.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/fancy_getopt.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/file_util.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/filelist.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/log.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/msvc9compiler.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/msvccompiler.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/py35compat.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/py38compat.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/spawn.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/sysconfig.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/text_file.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/unixccompiler.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/util.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/version.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_distutils/versionpredicate.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_imp.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/__init__.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/__init__.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/more.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/recipes.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/ordered_set.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/__about__.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/__init__.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_compat.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_structures.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_typing.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/markers.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/requirements.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/specifiers.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/tags.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/utils.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/version.py'
rm 'venv/lib/python3.9/site-packages/setuptools/_vendor/pyparsing.py'
rm 'venv/lib/python3.9/site-packages/setuptools/archive_util.py'
rm 'venv/lib/python3.9/site-packages/setuptools/build_meta.py'
rm 'venv/lib/python3.9/site-packages/setuptools/cli-32.exe'
rm 'venv/lib/python3.9/site-packages/setuptools/cli-64.exe'
rm 'venv/lib/python3.9/site-packages/setuptools/cli.exe'
rm 'venv/lib/python3.9/site-packages/setuptools/command/__init__.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/alias.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/bdist_egg.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/bdist_rpm.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/build_clib.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/build_ext.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/build_py.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/develop.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/dist_info.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/easy_install.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/egg_info.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/install.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/install_egg_info.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/install_lib.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/install_scripts.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/launcher manifest.xml'
rm 'venv/lib/python3.9/site-packages/setuptools/command/py36compat.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/register.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/rotate.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/saveopts.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/sdist.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/setopt.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/test.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/upload.py'
rm 'venv/lib/python3.9/site-packages/setuptools/command/upload_docs.py'
rm 'venv/lib/python3.9/site-packages/setuptools/config.py'
rm 'venv/lib/python3.9/site-packages/setuptools/dep_util.py'
rm 'venv/lib/python3.9/site-packages/setuptools/depends.py'
rm 'venv/lib/python3.9/site-packages/setuptools/dist.py'
rm 'venv/lib/python3.9/site-packages/setuptools/errors.py'
rm 'venv/lib/python3.9/site-packages/setuptools/extension.py'
rm 'venv/lib/python3.9/site-packages/setuptools/extern/__init__.py'
rm 'venv/lib/python3.9/site-packages/setuptools/glob.py'
rm 'venv/lib/python3.9/site-packages/setuptools/gui-32.exe'
rm 'venv/lib/python3.9/site-packages/setuptools/gui-64.exe'
rm 'venv/lib/python3.9/site-packages/setuptools/gui.exe'
rm 'venv/lib/python3.9/site-packages/setuptools/installer.py'
rm 'venv/lib/python3.9/site-packages/setuptools/launch.py'
rm 'venv/lib/python3.9/site-packages/setuptools/monkey.py'
rm 'venv/lib/python3.9/site-packages/setuptools/msvc.py'
rm 'venv/lib/python3.9/site-packages/setuptools/namespaces.py'
rm 'venv/lib/python3.9/site-packages/setuptools/package_index.py'
rm 'venv/lib/python3.9/site-packages/setuptools/py34compat.py'
rm 'venv/lib/python3.9/site-packages/setuptools/sandbox.py'
rm 'venv/lib/python3.9/site-packages/setuptools/script (dev).tmpl'
rm 'venv/lib/python3.9/site-packages/setuptools/script.tmpl'
rm 'venv/lib/python3.9/site-packages/setuptools/unicode_utils.py'
rm 'venv/lib/python3.9/site-packages/setuptools/version.py'
rm 'venv/lib/python3.9/site-packages/setuptools/wheel.py'
rm 'venv/lib/python3.9/site-packages/setuptools/windows_support.py'
rm 'venv/pyvenv.cfg'
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git add .
git commit -m "Remove virtual environment and clean up repository"

[main c6e950c] Remove virtual environment and clean up repository
 573 files changed, 14 insertions(+), 209589 deletions(-)
 delete mode 100644 venv/bin/Activate.ps1
 delete mode 100644 venv/bin/activate
 delete mode 100644 venv/bin/activate.csh
 delete mode 100644 venv/bin/activate.fish
 delete mode 100755 venv/bin/pip
 delete mode 100755 venv/bin/pip3
 delete mode 100755 venv/bin/pip3.9
 delete mode 120000 venv/bin/python
 delete mode 120000 venv/bin/python3
 delete mode 120000 venv/bin/python3.9
 delete mode 100644 venv/lib/python3.9/site-packages/_distutils_hack/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/_distutils_hack/override.py
 delete mode 100644 venv/lib/python3.9/site-packages/distutils-precedence.pth
 delete mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/INSTALLER
 delete mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/LICENSE.txt
 delete mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/METADATA
 delete mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/RECORD
 delete mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/REQUESTED
 delete mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/WHEEL
 delete mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/entry_points.txt
 delete mode 100644 venv/lib/python3.9/site-packages/pip-21.2.4.dist-info/top_level.txt
 delete mode 100644 venv/lib/python3.9/site-packages/pip/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/__main__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/build_env.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cache.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/autocompletion.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/base_command.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/cmdoptions.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/command_context.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/main.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/main_parser.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/parser.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/progress_bars.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/req_command.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/spinners.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/cli/status_codes.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/cache.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/check.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/completion.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/configuration.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/debug.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/download.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/freeze.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/hash.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/help.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/index.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/install.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/list.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/search.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/show.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/uninstall.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/commands/wheel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/configuration.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/distributions/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/distributions/base.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/distributions/installed.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/distributions/sdist.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/distributions/wheel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/exceptions.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/index/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/index/collector.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/index/package_finder.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/index/sources.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/locations/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/locations/_distutils.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/locations/_sysconfig.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/locations/base.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/main.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/metadata/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/metadata/base.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/metadata/pkg_resources.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/candidate.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/direct_url.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/format_control.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/index.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/link.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/scheme.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/search_scope.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/selection_prefs.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/target_python.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/models/wheel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/auth.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/cache.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/download.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/lazy_wheel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/session.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/utils.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/network/xmlrpc.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/build/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/build/metadata.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/build/metadata_legacy.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/build/wheel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/build/wheel_legacy.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/check.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/freeze.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/install/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/install/editable_legacy.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/install/legacy.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/install/wheel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/operations/prepare.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/pyproject.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/constructors.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/req_file.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/req_install.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/req_set.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/req_tracker.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/req/req_uninstall.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/base.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/legacy/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/legacy/resolver.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/base.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/candidates.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/factory.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/provider.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/reporter.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/requirements.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/resolution/resolvelib/resolver.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/self_outdated_check.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/_log.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/appdirs.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/compatibility_tags.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/datetime.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/deprecation.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/direct_url_helpers.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/distutils_args.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/encoding.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/entrypoints.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/filesystem.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/filetypes.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/glibc.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/hashes.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/inject_securetransport.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/logging.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/misc.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/models.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/packaging.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/parallel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/pkg_resources.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/setuptools_build.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/subprocess.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/temp_dir.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/unpacking.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/urls.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/virtualenv.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/utils/wheel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/vcs/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/vcs/bazaar.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/vcs/git.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/vcs/mercurial.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/vcs/subversion.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/vcs/versioncontrol.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_internal/wheel_builder.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/appdirs.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/_cmd.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/adapter.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/cache.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/file_cache.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/caches/redis_cache.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/controller.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/filewrapper.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/heuristics.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/serialize.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/cachecontrol/wrapper.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/certifi/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/certifi/__main__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/certifi/cacert.pem
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/certifi/core.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/big5freq.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/big5prober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/chardistribution.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/charsetgroupprober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/charsetprober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/cli/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/cli/chardetect.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/codingstatemachine.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/cp949prober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/enums.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/escprober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/escsm.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/eucjpprober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/euckrfreq.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/euckrprober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/euctwfreq.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/euctwprober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/gb2312freq.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/gb2312prober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/hebrewprober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/jisfreq.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/jpcntx.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langbulgarianmodel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langgreekmodel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langhebrewmodel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langhungarianmodel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langrussianmodel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langthaimodel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/langturkishmodel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/latin1prober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcharsetprober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcsgroupprober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/mbcssm.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/metadata/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/metadata/languages.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/sbcharsetprober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/sbcsgroupprober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/sjisprober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/universaldetector.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/utf8prober.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/chardet/version.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/colorama/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/colorama/ansi.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/colorama/ansitowin32.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/colorama/initialise.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/colorama/win32.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/colorama/winterm.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/misc.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/shutil.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/sysconfig.cfg
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/sysconfig.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/_backport/tarfile.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/database.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/index.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/locators.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/manifest.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/markers.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/metadata.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/resources.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/scripts.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/t32.exe
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/t64.exe
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/util.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/version.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/w32.exe
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/w64.exe
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distlib/wheel.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/distro.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_ihatexml.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_inputstream.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_tokenizer.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/_base.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_trie/py.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/_utils.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/constants.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/alphabeticalattributes.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/base.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/inject_meta_charset.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/lint.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/optionaltags.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/sanitizer.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/filters/whitespace.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/html5parser.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/serializer.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/genshi.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treeadapters/sax.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/base.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/dom.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/etree.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treebuilders/etree_lxml.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/base.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/dom.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/etree.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/etree_lxml.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/html5lib/treewalkers/genshi.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/codec.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/core.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/idnadata.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/intranges.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/package_data.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/idna/uts46data.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/msgpack/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/msgpack/_version.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/msgpack/exceptions.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/msgpack/ext.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/msgpack/fallback.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/__about__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/_manylinux.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/_musllinux.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/_structures.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/markers.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/requirements.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/specifiers.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/tags.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/utils.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/packaging/version.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/build.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/check.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/colorlog.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/dirtools.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/envbuild.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/in_process/_in_process.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/meta.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pep517/wrappers.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pkg_resources/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pkg_resources/py31compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/progress/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/progress/bar.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/progress/counter.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/progress/spinner.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/pyparsing.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/__version__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/_internal_utils.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/adapters.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/api.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/auth.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/certs.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/cookies.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/exceptions.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/help.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/hooks.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/models.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/packages.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/sessions.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/status_codes.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/structures.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/requests/utils.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/compat/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/compat/collections_abc.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/providers.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/reporters.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/resolvers.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/resolvelib/structs.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/six.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/_asyncio.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/_utils.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/after.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/before.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/before_sleep.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/nap.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/retry.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/stop.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/tornadoweb.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tenacity/wait.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tomli/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tomli/_parser.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/tomli/_re.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/_collections.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/_version.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/connection.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/connectionpool.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_appengine_environ.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/bindings.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/_securetransport/low_level.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/appengine.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/ntlmpool.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/pyopenssl.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/securetransport.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/contrib/socks.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/exceptions.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/fields.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/filepost.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/backports/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/backports/makefile.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/six.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/ssl_match_hostname/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/packages/ssl_match_hostname/_implementation.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/poolmanager.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/request.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/response.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/connection.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/proxy.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/queue.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/request.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/response.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/retry.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/ssl_.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/ssltransport.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/timeout.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/url.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/urllib3/util/wait.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/vendor.txt
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/webencodings/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/webencodings/labels.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/webencodings/mklabels.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/webencodings/tests.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/_vendor/webencodings/x_user_defined.py
 delete mode 100644 venv/lib/python3.9/site-packages/pip/py.typed
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/appdirs.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/__about__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_structures.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/_typing.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/markers.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/requirements.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/specifiers.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/tags.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/utils.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/packaging/version.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/_vendor/pyparsing.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/extern/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/pkg_resources/tests/data/my-test-package-source/setup.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/INSTALLER
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/LICENSE
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/METADATA
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/RECORD
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/REQUESTED
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/WHEEL
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/entry_points.txt
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools-58.0.4.dist-info/top_level.txt
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_deprecation_warning.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/_msvccompiler.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/archive_util.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/bcppcompiler.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/ccompiler.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/cmd.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_dumb.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_msi.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_rpm.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/bdist_wininst.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/build.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_clib.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_ext.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_py.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/build_scripts.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/check.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/clean.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/config.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/install.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_data.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_egg_info.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_headers.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_lib.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/install_scripts.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/py37compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/register.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/sdist.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/command/upload.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/config.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/core.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/cygwinccompiler.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/debug.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/dep_util.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/dir_util.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/dist.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/errors.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/extension.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/fancy_getopt.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/file_util.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/filelist.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/log.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/msvc9compiler.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/msvccompiler.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/py35compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/py38compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/spawn.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/sysconfig.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/text_file.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/unixccompiler.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/util.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/version.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_distutils/versionpredicate.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_imp.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/more.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/more_itertools/recipes.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/ordered_set.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/__about__.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_structures.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/_typing.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/markers.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/requirements.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/specifiers.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/tags.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/utils.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/packaging/version.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/_vendor/pyparsing.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/archive_util.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/build_meta.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/cli-32.exe
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/cli-64.exe
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/cli.exe
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/alias.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/bdist_egg.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/bdist_rpm.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/build_clib.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/build_ext.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/build_py.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/develop.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/dist_info.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/easy_install.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/egg_info.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/install.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/install_egg_info.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/install_lib.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/install_scripts.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/launcher manifest.xml
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/py36compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/register.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/rotate.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/saveopts.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/sdist.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/setopt.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/test.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/upload.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/command/upload_docs.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/config.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/dep_util.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/depends.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/dist.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/errors.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/extension.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/extern/__init__.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/glob.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/gui-32.exe
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/gui-64.exe
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/gui.exe
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/installer.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/launch.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/monkey.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/msvc.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/namespaces.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/package_index.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/py34compat.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/sandbox.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/script (dev).tmpl
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/script.tmpl
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/unicode_utils.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/version.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/wheel.py
 delete mode 100644 venv/lib/python3.9/site-packages/setuptools/windows_support.py
 delete mode 100644 venv/pyvenv.cfg
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/phishing-url-detector.git
git push -u origin main

remote: Repository not found.
fatal: repository 'https://github.com/YOUR_USERNAME/phishing-url-detector.git/' not found
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git branch -M main
git remote add origin https://github.com/Tawheed30/phishing-url-detector.git
git push -u origin main

error: remote origin already exists.
remote: Repository not found.
fatal: repository 'https://github.com/YOUR_USERNAME/phishing-url-detector.git/' not found
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git remote remove origin

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git remote add origin https://github.com/Tawheed30/phishing-url-detector.git

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git remote -v

origin	https://github.com/Tawheed30/phishing-url-detector.git (fetch)
origin	https://github.com/Tawheed30/phishing-url-detector.git (push)
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git push -u origin main

Enumerating objects: 638, done.
Counting objects: 100% (638/638), done.
Delta compression using up to 11 threads
Compressing objects: 100% (620/620), done.
Writing objects: 100% (638/638), 1.89 MiB | 1.37 MiB/s, done.
Total 638 (delta 47), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (47/47), done.
To https://github.com/Tawheed30/phishing-url-detector.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git clone https://github.com/Tawheed30/phishing-url-detector.git
cd phishing-url-detector

Cloning into 'phishing-url-detector'...
remote: Enumerating objects: 638, done.
remote: Counting objects: 100% (638/638), done.
remote: Compressing objects: 100% (573/573), done.
remote: Total 638 (delta 47), reused 638 (delta 47), pack-reused 0 (from 0)
Receiving objects: 100% (638/638), 1.89 MiB | 426.00 KiB/s, done.
Resolving deltas: 100% (47/47), done.
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 -m venv venv
source venv/bin/activate

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 -m venv venv
source venv/bin/activate

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % pip install -r requirements.txt

WARNING: You are using pip version 21.2.4; however, version 25.3 is available.
You should consider upgrading via the '/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/bin/python3 -m pip install --upgrade pip' command.
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % git add README.md
git commit -m "Add professional README"
git push

On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
Everything up-to-date
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % mkdir ml

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % mkdir ml

mkdir: ml: File exists
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % ml/phishing_dataset.csv

zsh: no such file or directory: ml/phishing_dataset.csv
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % ml/phishing_dataset.csv

zsh: no such file or directory: ml/phishing_dataset.csv
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % pwd 
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % cd ..

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % pwd 
/Users/mohammedtawheed/Documents/phishing-url-detector
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % mkdir -p ml

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano ml/phishing_dataset.csv

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % ls ml
phishing_dataset.csv
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano ml/train_model.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % pip install pandas scikit-learn

Collecting pandas
  Using cached pandas-2.3.3-cp39-cp39-macosx_11_0_arm64.whl (10.8 MB)
Collecting scikit-learn
  Downloading scikit_learn-1.6.1-cp39-cp39-macosx_12_0_arm64.whl (11.1 MB)
     |████████████████████████████████| 11.1 MB 22.5 MB/s 
Collecting python-dateutil>=2.8.2
  Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Collecting tzdata>=2022.7
  Using cached tzdata-2025.3-py2.py3-none-any.whl (348 kB)
Collecting numpy>=1.22.4
  Using cached numpy-2.0.2-cp39-cp39-macosx_14_0_arm64.whl (5.3 MB)
Collecting pytz>=2020.1
  Using cached pytz-2025.2-py2.py3-none-any.whl (509 kB)
Collecting joblib>=1.2.0
  Downloading joblib-1.5.3-py3-none-any.whl (309 kB)
     |████████████████████████████████| 309 kB 207 kB/s 
Collecting scipy>=1.6.0
  Downloading scipy-1.13.1-cp39-cp39-macosx_12_0_arm64.whl (30.3 MB)
     |████████████████████████████████| 30.3 MB 1.4 MB/s 
Collecting threadpoolctl>=3.1.0
  Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Collecting six>=1.5
  Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, numpy, tzdata, threadpoolctl, scipy, pytz, python-dateutil, joblib, scikit-learn, pandas
Successfully installed joblib-1.5.3 numpy-2.0.2 pandas-2.3.3 python-dateutil-2.9.0.post0 pytz-2025.2 scikit-learn-1.6.1 scipy-1.13.1 six-1.17.0 threadpoolctl-3.6.0 tzdata-2025.3
WARNING: You are using pip version 21.2.4; however, version 25.3 is available.
You should consider upgrading via the '/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/bin/python3 -m pip install --upgrade pip' command.
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 ml/train_model.py

^CTraceback (most recent call last):
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/ml/train_model.py", line 2, in <module>
    from sklearn.linear_model import LogisticRegression
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/__init__.py", line 73, in <module>
    from .base import clone  # noqa: E402
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/base.py", line 19, in <module>
    from .utils._estimator_html_repr import _HTMLDocumentationLinkMixin, estimator_html_repr
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/__init__.py", line 15, in <module>
    from ._chunking import gen_batches, gen_even_slices
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/_chunking.py", line 11, in <module>
    from ._param_validation import Interval, validate_params
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/_param_validation.py", line 17, in <module>
    from .validation import _is_arraylike_not_scalar
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py", line 21, in <module>
    from ..utils._array_api import _asarray_with_order, _is_numpy_namespace, get_namespace
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/_array_api.py", line 17, in <module>
    from .fixes import parse_version
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/fixes.py", line 17, in <module>
    import scipy.stats
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/scipy/stats/__init__.py", line 606, in <module>
    from ._stats_py import *
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/scipy/stats/_stats_py.py", line 42, in <module>
    from scipy.optimize import milp, LinearConstraint
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/scipy/optimize/__init__.py", line 414, in <module>
    from ._minimize import *
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/scipy/optimize/_minimize.py", line 33, in <module>
    from ._slsqp_py import _minimize_slsqp
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/scipy/optimize/_slsqp_py.py", line 19, in <module>
    from scipy.optimize._slsqp import slsqp
KeyboardInterrupt

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 ml/train_model.py

✅ ML model trained and saved as phishing_model.pkl
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 ml/train_model.py

✅ ML model trained and saved as phishing_model.pkl
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/ml_detector.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 src/main.py

[SUSPICIOUS] http://192.168.1.10/login (Score: 5)
[SUSPICIOUS] https://secure-paypal.com.verify.account-update.ru (Score: 3)
[SAFE] https://google.com (Score: 0)
[SUSPICIOUS] http://free-gift-login.com (Score: 3)

Report saved to reports/phishing_report.txt
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % ls src

main.py			ml_detector.py		report_generator.py	rules.py		url_analyzer.py
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 src/main.py

  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 25
    score, reasons = analyze_url(url)
    ^
IndentationError: expected an indented block
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 src/main.py

Traceback (most recent call last):
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 50, in <module>
    main()
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 8, in main
    with open(DATA_FILE, "r") as file:
FileNotFoundError: [Errno 2] No such file or directory: 'data/urls.txt'
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % mkdir -p data

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano data/urls.txt

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % ls data
sample_urls.txt	urls.txt
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 src/main.py

[SUSPICIOUS] http://192.168.1.10/login (Score: 5)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] SAFE (Confidence: 0.0)
----------------------------------------
[SUSPICIOUS] https://secure-paypal.com.verify.account-update.ru (Score: 3)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] PHISHING (Confidence: 0.7)
----------------------------------------
[SAFE] https://google.com (Score: 0)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] SAFE (Confidence: 0.0)
----------------------------------------
[SUSPICIOUS] http://free-gift-login.com (Score: 3)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] SAFE (Confidence: 0.0)
----------------------------------------
Traceback (most recent call last):
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 50, in <module>
    main()
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 47, in main
    generate_report(results)
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/report_generator.py", line 13, in generate_report
    for url, score, status, reasons in results:
ValueError: too many values to unpack (expected 4)
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/report_generator.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 src/main.py

[SUSPICIOUS] http://192.168.1.10/login (Score: 5)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] SAFE (Confidence: 0.0)
----------------------------------------
[SUSPICIOUS] https://secure-paypal.com.verify.account-update.ru (Score: 3)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] PHISHING (Confidence: 0.7)
----------------------------------------
[SAFE] https://google.com (Score: 0)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] SAFE (Confidence: 0.0)
----------------------------------------
[SUSPICIOUS] http://free-gift-login.com (Score: 3)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] SAFE (Confidence: 0.0)
----------------------------------------
Report saved to reports/phishing_report.txt
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano .env

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano .gitignore

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % pip install requests python-dotenv
pip freeze > requirements.txt

Collecting requests
  Downloading requests-2.32.5-py3-none-any.whl (64 kB)
     |████████████████████████████████| 64 kB 520 kB/s 
Collecting python-dotenv
  Downloading python_dotenv-1.2.1-py3-none-any.whl (21 kB)
Collecting idna<4,>=2.5
  Downloading idna-3.11-py3-none-any.whl (71 kB)
     |████████████████████████████████| 71 kB 1.8 MB/s 
Collecting charset_normalizer<4,>=2
  Downloading charset_normalizer-3.4.4-cp39-cp39-macosx_10_9_universal2.whl (209 kB)
     |████████████████████████████████| 209 kB 2.0 MB/s 
Collecting urllib3<3,>=1.21.1
  Downloading urllib3-2.6.2-py3-none-any.whl (131 kB)
     |████████████████████████████████| 131 kB 6.5 MB/s 
Collecting certifi>=2017.4.17
  Downloading certifi-2025.11.12-py3-none-any.whl (159 kB)
     |████████████████████████████████| 159 kB 6.6 MB/s 
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests, python-dotenv
Successfully installed certifi-2025.11.12 charset-normalizer-3.4.4 idna-3.11 python-dotenv-1.2.1 requests-2.32.5 urllib3-2.6.2
WARNING: You are using pip version 21.2.4; however, version 25.3 is available.
You should consider upgrading via the '/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/bin/python3 -m pip install --upgrade pip' command.
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/threat_intel.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 src/main.py

  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 43
    print("-" * 40)
IndentationError: unexpected indent
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 src/main.py

/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
Traceback (most recent call last):
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 14, in <module>
    for url in urls:
NameError: name 'urls' is not defined
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/main.py   

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 src/main.py

/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
[SUSPICIOUS] http://192.168.1.10/login (Score: 5)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] SAFE (Confidence: 0.0)
[VT] Malicious: 0 | Suspicious: 0
----------------------------------------
[SUSPICIOUS] https://secure-paypal.com.verify.account-update.ru (Score: 3)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] PHISHING (Confidence: 0.7)
[VT] No data / API limit
----------------------------------------
[SAFE] https://google.com (Score: 0)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] SAFE (Confidence: 0.0)
[VT] No data / API limit
----------------------------------------
[SUSPICIOUS] http://free-gift-login.com (Score: 3)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] SAFE (Confidence: 0.0)
[VT] No data / API limit
----------------------------------------
Report saved to reports/phishing_report.txt
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % def decide_response(score, ml_label, ml_confidence, vt_malicious):
    """
    Returns automated SOC-style response decision
    """

    if vt_malicious > 0:
        return "BLOCK"

    if ml_label == 1 and ml_confidence >= 0.7:
        return "BLOCK"

    if score >= 3:
        return "MONITOR"

    return "ALLOW"

if if if> 
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/soar_engine.py
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3

Python 3.9.6 (default, Dec  2 2025, 07:27:58) 
[Clang 17.0.0 (clang-1700.6.3.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> from src.soar_engine import decide_response
>>> decide_response(5, 1, 0.8, 0)
'BLOCK'
>>> src/ml_predictor.py
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'src' is not defined
>>> exit()
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/ml_predictor.py                                                      


(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 src/main.py

/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
[SUSPICIOUS] http://192.168.1.10/login (Score: 5)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] SAFE (Confidence: 0.0)
[VT] Malicious: 0 | Suspicious: 0
----------------------------------------
[SUSPICIOUS] https://secure-paypal.com.verify.account-update.ru (Score: 3)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] PHISHING (Confidence: 0.7)
[VT] No data / API limit
----------------------------------------
[SAFE] https://google.com (Score: 0)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] SAFE (Confidence: 0.0)
[VT] No data / API limit
----------------------------------------
[SUSPICIOUS] http://free-gift-login.com (Score: 3)
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py:2739: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names
  warnings.warn(
[ML] SAFE (Confidence: 0.0)
[VT] No data / API limit
----------------------------------------
Report saved to reports/phishing_report.txt
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/main.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/main.py
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % UserWarning: X does not have valid feature names

zsh: command not found: UserWarning:
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % import pandas as pd

def predict_phishing_ml(url):
    features = extract_features(url)

    df = pd.DataFrame([features], columns=[
        "url_length",
        "has_ip",
        "has_https",
        "num_dots",
        "has_suspicious_words"
    ])

    prediction = model.predict(df)[0]
    confidence = max(model.predict_proba(df)[0])

    return prediction, round(confidence, 2)

zsh: command not found: import
zsh: no matches found: predict_phishing_ml(url):
zsh: missing delimiter for 'u' glob qualifier
zsh: unknown file attribute:  
zsh: no matches found: model.predict(df)[0]
zsh: no matches found: max(model.predict_proba(df)[0])
zsh: number expected
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/ml_detector.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 src/main.py

/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
[SUSPICIOUS] http://192.168.1.10/login (Score: 5)
Traceback (most recent call last):
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 60, in <module>
    main()
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 30, in main
    ml_label, ml_confidence = predict_phishing_ml(url)
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/ml_detector.py", line 26, in predict_phishing_ml
    prediction = model.predict(df)[0]
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/linear_model/_base.py", line 374, in predict
    scores = self.decision_function(X)
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/linear_model/_base.py", line 351, in decision_function
    X = validate_data(self, X, accept_sparse="csr", reset=False)
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py", line 2919, in validate_data
    _check_feature_names(_estimator, X, reset=reset)
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py", line 2777, in _check_feature_names
    raise ValueError(message)
ValueError: The feature names should match those that were passed during fit.
Feature names unseen at fit time:
- num_dots
Feature names seen at fit time, yet now missing:
- subdomain_count

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano src/ml_detector.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 src/main.py

/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
[SUSPICIOUS] http://192.168.1.10/login (Score: 5)
Traceback (most recent call last):
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 60, in <module>
    main()
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/main.py", line 30, in main
    ml_label, ml_confidence = predict_phishing_ml(url)
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/src/ml_detector.py", line 30, in predict_phishing_ml
    prediction = model.predict(df)[0]
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/linear_model/_base.py", line 374, in predict
    scores = self.decision_function(X)
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/linear_model/_base.py", line 351, in decision_function
    X = validate_data(self, X, accept_sparse="csr", reset=False)
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py", line 2919, in validate_data
    _check_feature_names(_estimator, X, reset=reset)
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/phishing-url-detector/venv/lib/python3.9/site-packages/sklearn/utils/validation.py", line 2777, in _check_feature_names
    raise ValueError(message)
ValueError: The feature names should match those that were passed during fit.
Feature names must be in the same order as they were in fit.

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano ml/train_model.py

(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % python3 ml/train_model.py

Traceback (most recent call last):
  File "/Users/mohammedtawheed/Documents/phishing-url-detector/ml/train_model.py", line 1, in <module>
    X = df[[
NameError: name 'df' is not defined
(venv) mohammedtawheed@Mohammeds-MacBook-Pro-2 phishing-url-detector % nano ml/train_model.py


  UW PICO 5.09                                                                                                       File: ml/train_model.py                                                                                                        Modified  

import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
  
# Load dataset
df = pd.read_csv("ml/phishing_dataset.csv")
  
# Features (ORDER MATTERS — DO NOT CHANGE)
X = df[[
    "url_length",
    "has_ip",
    "has_https",
    "subdomain_count",
    "has_suspicious_words"
]]

# Label
y = df["label"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save model
joblib.dump(model, "ml/phishing_model.pkl")

print("✅ ML model trained and saved as phishing_model.pkl")











































^G Get Help                               ^O WriteOut                               ^R Read File                              ^Y Prev Pg                                ^K Cut Text                               ^C Cur Pos                                
^X Exit                                   ^J Justify                                ^W Where is                               ^V Next Pg                                ^U UnCut Text                             ^T To Spell                               
