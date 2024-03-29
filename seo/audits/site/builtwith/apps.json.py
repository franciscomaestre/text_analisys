{
    "apps": {
        "1C-Bitrix": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "BITRIX_",
                "X-Powered-CMS": "Bitrix Site Manager"
            },
            "html": "(?:<link[^>]+components/bitrix|(?:src|href)=\"/bitrix/(?:js|templates))",
            "icon": "1C-Bitrix.png",
            "implies": "PHP",
            "script": "1c-bitrix",
            "website": "www.1c-bitrix.ru"
        },
        "1und1": {
            "cats": [
                6
            ],
            "icon": "1und1.png",
            "implies": "PHP",
            "url": "/shop/catalog/browse\\?sessid=",
            "website": "1und1.de"
        },
        "2z Project": {
            "cats": [
                1
            ],
            "icon": "2z Project.png",
            "meta": {
                "generator": "2z project ([\\d.]+)\\;version:\\1"
            },
            "website": "2zproject-cms.ru"
        },
        "3DM": {
            "cats": [
                19
            ],
            "html": "<title>3ware 3DM([\\d\\.]+)?\\;version:\\1",
            "icon": "3DM.png",
            "implies": "3ware",
            "website": "www.3ware.com"
        },
        "3dCart": {
            "cats": [
                1,
                6
            ],
            "headers": {
                "Set-Cookie": "3dvisit",
                "X-Powered-By": "3DCART"
            },
            "icon": "3dCart.png",
            "script": "(?:twlh(?:track)?\\.asp|3d_upsell\\.js)",
            "website": "www.3dcart.com"
        },
        "3ware": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "3ware\\/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "3ware.png",
            "website": "www.3ware.com"
        },
        "AMPcms": {
            "cats": [
                1
            ],
            "env": "^amp_js_init$",
            "headers": {
                "Set-Cookie": "^AMP=",
                "X-AMP-Version": "([\\d.]+)\\;version:\\1"
            },
            "icon": "AMPcms.png",
            "implies": "PHP",
            "website": "www.ampcms.org"
        },
        "AOLserver": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "AOLserver/?([\\d.]+)?\\;version:\\1"
            },
            "icon": "AOLserver.png",
            "website": "aolserver.com"
        },
        "AT Internet Analyzer": {
            "cats": [
                10
            ],
            "env": "^xtsite$",
            "icon": "AT Internet Analyzer.png",
            "website": "atinternet.com/en"
        },
        "AT Internet XiTi": {
            "cats": [
                10
            ],
            "env": "^Xt_",
            "icon": "AT Internet XiTi.png",
            "script": "xiti\\.com/hit\\.xiti",
            "website": "atinternet.com/en"
        },
        "ATEN": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "ATEN HTTP Server(?:\\(?V?([\\d\\.]+)\\)?)?\\;version:\\1"
            },
            "icon": "ATEN.png",
            "website": "www.aten.com"
        },
        "AWStats": {
            "cats": [
                10
            ],
            "icon": "AWStats.png",
            "implies": "Perl",
            "meta": {
                "generator": "AWStats ([\\d.]+(?: \\(build [\\d.]+\\))?)\\;version:\\1"
            },
            "website": "awstats.sourceforge.net"
        },
        "Accessible Portal": {
            "cats": [
                1
            ],
            "icon": "Accessible Portal.png",
            "implies": "PHP",
            "meta": {
                "generator": "Accessible Portal"
            },
            "website": "www.accessibleportal.com"
        },
        "AdInfinity": {
            "cats": [
                36
            ],
            "icon": "AdInfinity.png",
            "script": "adinfinity\\.com\\.au",
            "website": "adinfinity.com.au"
        },
        "AdRiver": {
            "cats": [
                36
            ],
            "env": "^adriver$",
            "html": "(?:<embed[^>]+(?:src=\"https?://mh\\d?\\.adriver\\.ru/|flashvars=\"[^\"]*(?:http:%3A//(?:ad|mh\\d?)\\.adriver\\.ru/|adriver_banner))|<(?:(?:iframe|img)[^>]+src|a[^>]+href)=\"https?://ad\\.adriver\\.ru/)",
            "icon": "AdRiver.png",
            "script": "(?:adriver\\.core\\.\\d\\.js|https?://(?:content|ad|masterh\\d)\\.adriver\\.ru/)",
            "website": "adriver.ru"
        },
        "AdRoll": {
            "cats": [
                36
            ],
            "env": "^adroll_",
            "icon": "AdRoll.png",
            "script": "(?:a|s)\\.adroll\\.com",
            "website": "adroll.com"
        },
        "Adcash": {
            "cats": [
                36
            ],
            "env": "^(?:ac_bgclick_URL|ct_(?:siteunder|tag|n(?:SuUrl(?:Opp)?)|Su(?:Loaded|Url)))$",
            "icon": "Adcash.png",
            "script": "^[^\\/]*//(?:[^\\/]+\\.)?adcash\\.com/(?:script|ad)/",
            "url": "^https?://(?:[^\\/]+\\.)?adcash\\.com/script/pop_",
            "website": "adcash.com"
        },
        "AddShoppers": {
            "cats": [
                5
            ],
            "icon": "AddShoppers.png",
            "script": "cdn\\.shop\\.pe/widget/",
            "website": "www.addshoppers.com"
        },
        "AddThis": {
            "cats": [
                5
            ],
            "env": "^addthis",
            "icon": "AddThis.png",
            "script": "addthis\\.com/js/",
            "website": "www.addthis.com"
        },
        "AddToAny": {
            "cats": [
                5
            ],
            "env": "^a2apage_init$",
            "icon": "AddToAny.png",
            "script": "addtoany\\.com/menu/page\\.js",
            "website": "www.addtoany.com"
        },
        "Adobe ColdFusion": {
            "cats": [
                18
            ],
            "env": "^_cfEmails$",
            "headers": {
                "Cookie": "CFTOKEN="
            },
            "html": "<!-- START headerTags\\.cfm",
            "icon": "Adobe ColdFusion.png",
            "implies": "CFML",
            "script": "/cfajax/",
            "url": "\\.cfm(?:$|\\?)",
            "website": "adobe.com/products/coldfusion-family.html"
        },
        "Adobe Experience Manager": {
            "cats": [
                1
            ],
            "html": [
                "<div class=\"[^\"]*parbase",
                "<div[^>]+data-component-path=\"[^\"+]jcr:"
            ],
            "icon": "Adobe Experience Manager.png",
            "implies": "Java",
            "script": "/etc/designs/",
            "website": "www.adobe.com/au/marketing-cloud/enterprise-content-management.html"
        },
        "Adobe GoLive": {
            "cats": [
                20
            ],
            "icon": "Adobe GoLive.png",
            "meta": {
                "generator": "Adobe GoLive(?:\\s([\\d.]+))?\\;version:\\1"
            },
            "website": "www.adobe.com/products/golive"
        },
        "Adobe Muse": {
            "cats": [
                20
            ],
            "icon": "Adobe Muse.png",
            "meta": {
                "generator": "^Muse(?:$| ?/?(\\d[\\d.]+))\\;version:\\1"
            },
            "website": "muse.adobe.com"
        },
        "Adobe RoboHelp": {
            "cats": [
                4
            ],
            "env": "^gbWh(?:Ver|Lang|Msg|Util|Proxy)$",
            "icon": "Adobe RoboHelp.png",
            "meta": {
                "generator": "^Adobe RoboHelp(?: ([\\d]+))?\\;version:\\1"
            },
            "script": "(?:wh(?:utils|ver|proxy|lang|topic|msg)|ehlpdhtm)\\.js",
            "website": "adobe.com/products/robohelp.html"
        },
        "Advanced Web Stats": {
            "cats": [
                10
            ],
            "html": "aws\\.src = [^<]+caphyon-analytics",
            "icon": "Advanced Web Stats.png",
            "implies": "Java",
            "website": "www.advancedwebstats.com"
        },
        "Advert Stream": {
            "cats": [
                36
            ],
            "env": "^advst_is_above_the_fold$",
            "icon": "Advert Stream.png",
            "script": "(?:ad\\.advertstream\\.com|adxcore\\.com)",
            "website": "www.advertstream.com"
        },
        "Adzerk": {
            "cats": [
                36
            ],
            "env": "^ados(?:Results)?$",
            "html": "<iframe [^>]*src=\"[^\"]+adzerk\\.net",
            "icon": "Adzerk.png",
            "script": "adzerk\\.net/ados\\.js",
            "website": "adzerk.com"
        },
        "Aegea": {
            "cats": [
                11
            ],
            "headers": {
                "X-Powered-By": "^E2 Aegea v(\\d+)$\\;version:\\1"
            },
            "icon": "Aegea.png",
            "implies": [
                "PHP",
                "jQuery"
            ],
            "website": "blogengine.ru"
        },
        "AfterBuy": {
            "cats": [
                6
            ],
            "html": [
                "<dd>This OnlineStore is brought to you by ViA-Online GmbH Afterbuy. Information and contribution at https://www.afterbuy.de</dd>"
            ],
            "icon": "after-buy.png",
            "script": "shop-static\\.afterbuy\\.de",
            "website": "www.afterbuy.de"
        },
        "Airee": {
            "cats": [
                31
            ],
            "headers": {
                "Server": "Airee"
            },
            "icon": "Airee.png",
            "website": "xn--80aqc2a.xn--p1ai"
        },
        "Akamai": {
            "cats": [
                31
            ],
            "headers": {
                "X-Akamai-Transformed": ""
            },
            "icon": "Akamai.png",
            "website": "akamai.com"
        },
        "Algolia Realtime Search": {
            "cats": [
                29
            ],
            "env": "^AlgoliaSearch$",
            "icon": "Algolia Realtime Search.png",
            "website": "www.algolia.com"
        },
        "Allegro RomPager": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Allegro-Software-RomPager(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Allegro RomPager.png",
            "website": "allegrosoft.com/embedded-web-server-s2"
        },
        "AlloyUI": {
            "cats": [
                12
            ],
            "env": "^AUI$",
            "icon": "AlloyUI.png",
            "implies": [
                "Twitter Bootstrap",
                "YUI"
            ],
            "script": "^https?://cdn\\.alloyui\\.com/",
            "website": "www.alloyui.com"
        },
        "Amaya": {
            "cats": [
                20
            ],
            "icon": "Amaya.png",
            "meta": {
                "generator": "Amaya(?: V?([\\d.]+[a-z]))?\\;version:\\1"
            },
            "website": "www.w3.org/Amaya"
        },
        "Ametys": {
            "cats": [
                1
            ],
            "icon": "Ametys.png",
            "implies": "Java",
            "meta": {
                "generator": "(?:Ametys|Anyware Technologies)"
            },
            "script": "ametys\\.js",
            "website": "ametys.org"
        },
        "Amiro.CMS": {
            "cats": [
                1
            ],
            "icon": "Amiro.CMS.png",
            "implies": "PHP",
            "meta": {
                "generator": "Amiro"
            },
            "website": "amirocms.com"
        },
        "Anchor CMS": {
            "cats": [
                1,
                11
            ],
            "icon": "Anchor CMS.png",
            "implies": [
                "PHP",
                "MySQL"
            ],
            "meta": {
                "generator": "Anchor CMS"
            },
            "website": "anchorcms.com"
        },
        "Angular Material": {
            "cats": [
                18
            ],
            "env": "^angular$",
            "icon": "Angular.svg",
            "implies": [
                "AngularJS"
            ],
            "script": [
                "/([\\d.]+(?:\\-?rc[.\\d]*)*)/angular-material(?:\\.min)?\\.js\\;version:\\1",
                "angular-material.*\\.js"
            ],
            "website": "material.angularjs.org"
        },
        "AngularJS": {
            "cats": [
                12
            ],
            "env": "^angular$",
            "icon": "AngularJS.png",
            "script": [
                "angular(?:\\-|\\.)([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
                "/([\\d.]+(?:\\-?rc[.\\d]*)*)/angular(?:\\.min)?\\.js\\;version:\\1",
                "angular.*\\.js"
            ],
            "website": "angularjs.org"
        },
        "Apache": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "(?:Apache(?:$|/([\\d.]+)|[^/-])|(?:^|\b)HTTPD)\\;version:\\1"
            },
            "icon": "Apache.svg",
            "website": "apache.org"
        },
        "Apache HBase": {
            "cats": [
                34
            ],
            "html": "<style[^>]+static/hbase",
            "icon": "Apache HBase.png",
            "website": "hbase.apache.org"
        },
        "Apache Hadoop": {
            "cats": [
                34
            ],
            "html": "<style[^>]+static/hadoop",
            "icon": "Apache Hadoop.png",
            "website": "hadoop.apache.org"
        },
        "Apache JSPWiki": {
            "cats": [
                8
            ],
            "html": "<html[^>]* xmlns:jspwiki=",
            "icon": "Apache JSPWiki.png",
            "script": "jspwiki",
            "url": "wiki\\.jsp",
            "website": "jspwiki.org"
        },
        "Apache Tomcat": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Apache-Coyote(/1\\.1)?\\;version:\\1?4.1+:",
                "X-Powered-By": "\bTomcat\b(?:-([\\d.]+))?\\;version:\\1"
            },
            "icon": "Apache Tomcat.png",
            "website": "tomcat.apache.org"
        },
        "Apache Traffic Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "ATS/?([\\d.]+)?\\;version:\\1"
            },
            "icon": "Apache Traffic Server.png",
            "website": "trafficserver.apache.org/"
        },
        "Apache Wicket": {
            "cats": [
                18
            ],
            "env": "^Wicket",
            "icon": "Apache Wicket.png",
            "implies": "Java",
            "website": "wicket.apache.org"
        },
        "AppNexus": {
            "cats": [
                36
            ],
            "html": "<(?:iframe|img)[^>]+adnxs\\.(?:net|com)",
            "icon": "AppNexus.png",
            "script": "adnxs\\.(?:net|com)",
            "website": "appnexus.com"
        },
        "Arastta": {
            "cats": [
                6
            ],
            "excludes": "OpenCart",
            "headers": {
                "Arastta": "(.*)\\;version:\\1",
                "X-Arastta": ""
            },
            "html": "Powered by <a [^>]*href=\"https?://(?:www\\.)?arastta\\.org[^>]+>Arastta",
            "icon": "Arastta.png",
            "implies": "PHP",
            "script": "arastta\\.js",
            "website": "arastta.org"
        },
        "Arc Forum": {
            "cats": [
                2
            ],
            "html": "ping\\.src = node\\.href;\\s+[^>]+\\s+}\\s+</script>",
            "icon": "Arc Forum.png",
            "website": "arclanguage.org"
        },
        "Artifactory": {
            "cats": [
                47
            ],
            "env": "^ArtifactoryUpdates$",
            "html": [
                "<span class=\"version\">Artifactory(?: Pro)?(?: Power Pack)?(?: ([\\d.]+))?\\;version:\\1"
            ],
            "icon": "Artifactory.png",
            "script": [
                "wicket/resource/org\\.artifactory\\."
            ],
            "website": "jfrog.com/open-source/#os-arti"
        },
        "Artifactory Web Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Artifactory(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Artifactory Web Server.png",
            "implies": [
                "Artifactory"
            ],
            "website": "jfrog.com/open-source/#os-arti"
        },
        "ArvanCloud": {
            "cats": [
                31
            ],
            "env": "^ArvanCloud$",
            "headers": {
                "AR-PoweredBy": "Arvan Cloud \\(arvancloud.com\\)"
            },
            "icon": "ArvanCloud.png",
            "website": "www.ArvanCloud.com"
        },
        "AsciiDoc": {
            "cats": [
                1,
                20,
                27
            ],
            "env": "^asciidoc$",
            "icon": "AsciiDoc.png",
            "meta": {
                "generator": "^AsciiDoc ([\\d.]+)\\;version:\\1"
            },
            "website": "www.methods.co.nz/asciidoc"
        },
        "Asymptix PHP Framework": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "Asymptix PHP Framework(?:.*)"
            },
            "html": [
                "Powered by <a href=\"http://www.asymptix.com/\" rel=\"external\">Asymptix PHP Framework</a>"
            ],
            "icon": "Asymptix PHP Framework.png",
            "implies": [
                "PHP"
            ],
            "website": "github.com/Asymptix/Framework"
        },
        "Atlassian Bitbucket": {
            "cats": [
                47
            ],
            "env": "^bitbucket$",
            "icon": "Atlassian Bitbucket.png",
            "meta": {
                "application-name": "Bitbucket"
            },
            "website": "www.atlassian.com/software/bitbucket/overview/"
        },
        "Atlassian Confluence": {
            "cats": [
                8
            ],
            "headers": {
                "X-Confluence-Request-Time": ""
            },
            "html": "Powered by <a href=[^>]+atlassian\\.com/software/confluence(?:[^>]+>Atlassian Confluence</a> ([\\d.]+))?\\;version:\\1",
            "icon": "Atlassian Confluence.png",
            "implies": "Java",
            "meta": {
                "confluence-request-time": ""
            },
            "website": "www.atlassian.com/software/confluence/overview/team-collaboration-software"
        },
        "Atlassian FishEye": {
            "cats": [
                47
            ],
            "headers": {
                "Set-cookie": "FESESSIONID"
            },
            "html": "<title>(?:Log in to )?FishEye (?:and Crucible )?([\\d.]+)?</title>\\;version:\\1",
            "icon": "Atlassian FishEye.png",
            "website": "www.atlassian.com/software/fisheye/overview/"
        },
        "Atlassian Jira": {
            "cats": [
                13
            ],
            "env": "^jira$",
            "html": "Powered by\\s+<a href=[^>]+atlassian\\.com/(?:software/jira|jira-bug-tracking/)[^>]+>Atlassian\\s+JIRA(?:[^v]*v(?:ersion: )?(\\d+\\.\\d+(?:\\.\\d+)?))?\\;version:\\1",
            "icon": "Atlassian Jira.png",
            "implies": "Java",
            "meta": {
                "ajs-version-number": "([\\d\\.]+)\\;version:\\1",
                "application-name": "JIRA"
            },
            "website": "www.atlassian.com/software/jira/overview/"
        },
        "Atlassian Jira Issue Collector": {
            "cats": [
                13,
                47
            ],
            "icon": "Atlassian Jira Issue Collector.png",
            "script": [
                "jira-issue-collector-plugin",
                "atlassian\\.jira\\.collector\\.plugin"
            ],
            "website": "www.atlassian.com/software/jira/overview/"
        },
        "Avangate": {
            "cats": [
                6
            ],
            "env": "^(?:__)?avng8_",
            "html": "<link[^>]* href=\"^https?://edge\\.avangate\\.net/",
            "icon": "Avangate.png",
            "script": "^https?://edge\\.avangate\\.net/",
            "website": "avangate.com"
        },
        "BEM": {
            "cats": [
                12
            ],
            "html": "<[^>]+data-bem",
            "icon": "BEM.png",
            "website": "en.bem.info"
        },
        "BIGACE": {
            "cats": [
                1
            ],
            "html": "(?:Powered by <a href=\"[^>]+BIGACE|<!--\\s+Site is running BIGACE)",
            "icon": "BIGACE.png",
            "implies": "PHP",
            "meta": {
                "generator": "BIGACE ([\\d.]+)\\;version:\\1"
            },
            "website": "bigace.de"
        },
        "Backbone.js": {
            "cats": [
                12
            ],
            "env": "^Backbone$",
            "icon": "Backbone.js.png",
            "implies": "Underscore.js",
            "script": "backbone.*\\.js",
            "website": "backbonejs.org"
        },
        "Backdrop": {
            "cats": [
                1
            ],
            "env": "^Backdrop$",
            "excludes": "Drupal",
            "icon": "Backdrop.png",
            "implies": "PHP",
            "meta": {
                "generator": "Backdrop CMS(?: (\\d))?\\;version:\\1"
            },
            "website": "backdropcms.org"
        },
        "Banshee": {
            "cats": [
                1,
                18
            ],
            "html": "Built upon the <a href=\"[^>]+banshee-php\\.org/\">[a-z]+</a>(?:v([\\d.]+))?\\;version:\\1",
            "icon": "Banshee.png",
            "implies": "PHP",
            "meta": {
                "generator": "Banshee PHP"
            },
            "website": "www.banshee-php.org"
        },
        "BaseHTTP": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "BaseHTTP\\/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "BaseHTTP.png",
            "implies": "Python",
            "website": "docs.python.org/2/library/basehttpserver.html"
        },
        "BigDump": {
            "cats": [
                3
            ],
            "html": "<!-- <h1>BigDump: Staggered MySQL Dump Importer ver\\. ([\\d.b]+)\\;version:\\1",
            "icon": "default.png",
            "implies": [
                "MySQL",
                "PHP"
            ],
            "website": "www.ozerov.de/bigdump.php"
        },
        "Bigcommerce": {
            "cats": [
                6
            ],
            "env": "^compareProducts$",
            "html": "<link href=[^>]+cdn\\d+\\.bigcommerce\\.com/v",
            "icon": "Bigcommerce.svg",
            "script": "cdn\\d+\\.bigcommerce\\.com/v",
            "url": "mybigcommerce\\.com",
            "website": "www.bigcommerce.com"
        },
        "Bigware": {
            "cats": [
                6
            ],
            "headers": {
                "Set-Cookie": "(?:bigwareCsid|bigWAdminID)"
            },
            "html": "(?:Diese <a href=[^>]+bigware\\.de|<a href=[^>]+/main_bigware_\\d+\\.php)",
            "icon": "Bigware.png",
            "implies": "PHP",
            "url": "(?:\\?|&)bigWAdminID=",
            "website": "bigware.de"
        },
        "BittAds": {
            "cats": [
                36
            ],
            "env": "^bitt$",
            "icon": "BittAds.png",
            "script": "bittads\\.com/js/bitt\\.js$",
            "website": "bittads.com"
        },
        "Blesta": {
            "cats": [
                6
            ],
            "headers": {
                "Set-Cookie": "blesta_sid"
            },
            "icon": "Blesta.png",
            "website": "www.blesta.com"
        },
        "Blip.tv": {
            "cats": [
                14
            ],
            "html": "<(?:param|embed|iframe)[^>]+blip\\.tv/play",
            "icon": "Blip.tv.png",
            "website": "blip.tv"
        },
        "Blogger": {
            "cats": [
                11
            ],
            "icon": "Blogger.png",
            "meta": {
                "generator": "blogger"
            },
            "url": "\\.blogspot\\.com",
            "website": "www.blogger.com"
        },
        "Bluefish": {
            "cats": [
                20
            ],
            "icon": "Bluefish.png",
            "meta": {
                "generator": "Bluefish(?:\\s([\\d.]+))?\\;version:\\1"
            },
            "website": "sourceforge.net/projects/bluefish"
        },
        "Boa": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Boa\\/?([\\d\\.a-z]+)?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "www.boa.org"
        },
        "Boba.js": {
            "cats": [
                12
            ],
            "icon": "default.png",
            "implies": "Google Analytics",
            "script": "boba(?:\\.min)?\\.js",
            "website": "boba.space150.com"
        },
        "Bolt": {
            "cats": [
                1
            ],
            "icon": "Bolt.png",
            "implies": "PHP",
            "meta": {
                "generator": "Bolt"
            },
            "website": "bolt.cm"
        },
        "Bonfire": {
            "cats": [
                18
            ],
            "headers": {
                "Set-Cookie": "bf_session="
            },
            "html": "Powered by <a[^>]+href=\"https?://(?:www\\.)?cibonfire\\.com[^>]*>Bonfire v([^<]+)\\;version:\\1",
            "icon": "Bonfire.png",
            "implies": "CodeIgniter",
            "website": "cibonfire.com"
        },
        "Bounce Exchange": {
            "cats": [
                32
            ],
            "env": "^bouncex$",
            "html": "<script[^>]*>[^>]+\\.src\\s*=\\s*['\"](?:https?:)?//tag\\.bounceexchange\\.com/",
            "icon": "Bounce Exchange.svg",
            "script": "^https?://tag\\.bounceexchange\\.com/",
            "website": "www.bounceexchange.com"
        },
        "Brother": {
            "cats": [
                40
            ],
            "icon": "Brother.png",
            "website": "www.brother.com"
        },
        "BrowserCMS": {
            "cats": [
                1
            ],
            "icon": "BrowserCMS.png",
            "implies": "Ruby",
            "meta": {
                "generator": "BrowserCMS ([\\d.]+)\\;version:\\1"
            },
            "website": "browsercms.org"
        },
        "BugSense": {
            "cats": [
                10
            ],
            "env": "^BugSense$",
            "icon": "BugSense.png",
            "script": "bugsense\\.js",
            "website": "bugsense.com"
        },
        "BugSnag": {
            "cats": [
                10
            ],
            "env": "^BugSnag$",
            "icon": "BugSnag.png",
            "script": "bugsnag.*\\.js",
            "website": "bugsnag.com"
        },
        "Bugzilla": {
            "cats": [
                13
            ],
            "html": "href=\"enter_bug\\.cgi\">",
            "icon": "Bugzilla.png",
            "implies": "Perl",
            "website": "www.bugzilla.org"
        },
        "Burning Board": {
            "cats": [
                2
            ],
            "html": "<a href=\"[^>]+woltlab\\.com[^<]+<strong>Burning Board",
            "icon": "Burning Board.png",
            "implies": [
                "PHP",
                "Woltlab Community Framework"
            ],
            "website": "www.woltlab.com"
        },
        "Business Catalyst": {
            "cats": [
                1
            ],
            "html": "<!-- BC_OBNW -->",
            "icon": "Business Catalyst.png",
            "script": "CatalystScripts",
            "website": "businesscatalyst.com"
        },
        "BuySellAds": {
            "cats": [
                36
            ],
            "env": "^_bsa",
            "html": "<script[^>]*>[^<]+?bsa.src\\s*=\\s*['\"](?:https?:)?\\/{2}\\w\\d\\.buysellads\\.com\\/[\\w\\d\\/]+?bsa\\.js['\"]",
            "icon": "BuySellAds.png",
            "script": "^https?://s\\d\\.buysellads\\.com/",
            "website": "buysellads.com"
        },
        "C++": {
            "cats": [
                27
            ],
            "icon": "C++.png",
            "website": "isocpp.org"
        },
        "CFML": {
            "cats": [
                27
            ],
            "icon": "CFML.png",
            "website": "adobe.com/products/coldfusion-family.html"
        },
        "CKEditor": {
            "cats": [
                24
            ],
            "env": "^CKEDITOR$",
            "icon": "CKEditor.png",
            "website": "ckeditor.com"
        },
        "CMS Made Simple": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "^CMSSESSID"
            },
            "icon": "CMS Made Simple.png",
            "implies": "PHP",
            "meta": {
                "generator": "CMS Made Simple"
            },
            "website": "cmsmadesimple.org"
        },
        "CMSimple": {
            "cats": [
                1
            ],
            "icon": "default.png",
            "implies": "PHP",
            "meta": {
                "generator": "CMSimple( [\\d.]+)?\\;version:\\1"
            },
            "website": "www.cmsimple.org/en"
        },
        "CO2Stats": {
            "cats": [
                10
            ],
            "html": "src=[^>]+co2stats\\.com/propres\\.php",
            "icon": "CO2Stats.png",
            "website": "co2stats.com"
        },
        "CPG Dragonfly": {
            "cats": [
                1
            ],
            "headers": {
                "X-Powered-By": "Dragonfly CMS"
            },
            "icon": "CPG Dragonfly.png",
            "implies": "PHP",
            "meta": {
                "generator": "CPG Dragonfly"
            },
            "website": "dragonflycms.org"
        },
        "CS Cart": {
            "cats": [
                6
            ],
            "env": "^fn_compare_strings$",
            "html": [
                "&nbsp;Powered by (?:<a href=[^>]+cs-cart\\.com|CS-Cart)",
                ".cm-noscript[^>]+</style>"
            ],
            "icon": "CS Cart.png",
            "implies": "PHP",
            "website": "www.cs-cart.com"
        },
        "CacheFly": {
            "cats": [
                31
            ],
            "headers": {
                "Server": "^CFS ",
                "X-CF1": "",
                "X-CF2": ""
            },
            "icon": "CacheFly.png",
            "website": "www.cachefly.com"
        },
        "Caddy": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "^Caddy$"
            },
            "icon": "caddy.svg",
            "website": "caddyserver.com"
        },
        "CakePHP": {
            "cats": [
                18
            ],
            "headers": {
                "Set-Cookie": "cakephp="
            },
            "icon": "CakePHP.png",
            "implies": "PHP",
            "meta": {
                "application-name": "CakePHP"
            },
            "website": "cakephp.org"
        },
        "Canon": {
            "cats": [
                40
            ],
            "icon": "Canon.png",
            "website": "www.canon.com"
        },
        "Canon HTTP Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "CANON HTTP Server(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Canon HTTP Server.png",
            "implies": [
                "Canon"
            ],
            "website": "www.canon.com"
        },
        "Captch Me": {
            "cats": [
                16,
                36
            ],
            "env": "^Captchme",
            "icon": "Captch Me.svg",
            "script": "^https?://api\\.captchme\\.net/",
            "website": "captchme.com"
        },
        "Carbon Ads": {
            "cats": [
                36
            ],
            "env": "^_carbonads",
            "html": "<[a-z]+ [^>]*id=\"carbonads-container\"",
            "icon": "Carbon Ads.png",
            "script": "[^\\/]*\\/\\/(?:engine|srv)\\.carbonads\\.com\\/",
            "website": "carbonads.net"
        },
        "Cargo": {
            "cats": [
                1
            ],
            "html": "<link [^>]+Cargo feed",
            "icon": "Cargo.png",
            "implies": "PHP",
            "meta": {
                "cargo_title": ""
            },
            "script": "/cargo\\.",
            "website": "cargocollective.com"
        },
        "Catberry.js": {
            "cats": [
                12,
                18
            ],
            "env": "^catberry$",
            "headers": {
                "X-Powered-By": "Catberry"
            },
            "icon": "Catberry.js.png",
            "implies": "Node.js",
            "website": "catberry.org"
        },
        "Catwalk": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Catwalk\\/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "Catwalk.png",
            "implies": "Canon",
            "website": "www.canon.com"
        },
        "CentOS": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "CentOS",
                "X-Powered-By": "CentOS"
            },
            "icon": "CentOS.png",
            "website": "centos.org"
        },
        "CenteHTTPd": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "CenteHTTPd(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "CenteHTTPd.png",
            "website": "cente.jp/cente/app/HTTPdc.html"
        },
        "Chameleon": {
            "cats": [
                1
            ],
            "icon": "Chameleon.png",
            "implies": [
                "Apache",
                "PHP"
            ],
            "meta": {
                "generator": "chameleon-cms"
            },
            "website": "chameleon-system.de"
        },
        "Chamilo": {
            "cats": [
                21
            ],
            "headers": {
                "X-Powered-By": "Chamilo ([\\d.]+)\\;version:\\1"
            },
            "html": "\">Chamilo ([\\d.]+)</a>\\;version:\\1",
            "icon": "Chamilo.png",
            "implies": "PHP",
            "meta": {
                "generator": "Chamilo ([\\d.]+)\\;version:\\1"
            },
            "website": "www.chamilo.org"
        },
        "Chartbeat": {
            "cats": [
                10
            ],
            "env": "^_sf_(?:endpt|async_config)$",
            "icon": "Chartbeat.png",
            "script": "chartbeat\\.js",
            "website": "chartbeat.com"
        },
        "Cherokee": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Cherokee/([\\d.]+)\\;version:\\1"
            },
            "icon": "Cherokee.png",
            "website": "www.cherokee-project.com"
        },
        "CherryPy": {
            "cats": [
                18,
                22
            ],
            "headers": {
                "Server": "CherryPy\\/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "CherryPy.png",
            "implies": "Python",
            "website": "www.cherrypy.org"
        },
        "Chitika": {
            "cats": [
                36
            ],
            "env": "ch_c(?:lient|olor_site_link)",
            "icon": "Chitika.png",
            "script": "scripts\\.chitika\\.net/",
            "website": "chitika.com"
        },
        "Ckan": {
            "cats": [
                1
            ],
            "headers": {
                "Access-Control-Allow-Headers": "X-CKAN-API-KEY",
                "Link": "<http://ckan.org/>; rel=shortlink"
            },
            "icon": "Ckan.png",
            "implies": [
                "Python",
                "Solr",
                "Java",
                "PostgreSQL"
            ],
            "website": "ckan.org/"
        },
        "ClickHeat": {
            "cats": [
                10
            ],
            "env": "^clickHeat",
            "icon": "ClickHeat.png",
            "implies": "PHP",
            "script": "clickheat.*\\.js",
            "website": "www.labsmedia.com/clickheat/index.html"
        },
        "ClickTale": {
            "cats": [
                10
            ],
            "env": "^ClickTale",
            "icon": "ClickTale.png",
            "website": "www.clicktale.com"
        },
        "Clicky": {
            "cats": [
                10
            ],
            "env": "^clicky$",
            "icon": "Clicky.png",
            "script": "static\\.getclicky\\.com",
            "website": "getclicky.com"
        },
        "Clientexec": {
            "cats": [
                6
            ],
            "html": "clientexec\\.[^>]*\\s?=\\s?[^>]*;",
            "icon": "Clientexec.png",
            "website": "www.clientexec.com"
        },
        "CloudFlare": {
            "cats": [
                31
            ],
            "env": "^CloudFlare$",
            "headers": {
                "Server": "cloudflare"
            },
            "icon": "CloudFlare.svg",
            "website": "www.cloudflare.com"
        },
        "Cloudera": {
            "cats": [
                34
            ],
            "headers": {
                "Server": "cloudera"
            },
            "icon": "Cloudera.png",
            "website": "www.cloudera.com"
        },
        "CodeIgniter": {
            "cats": [
                18
            ],
            "headers": {
                "Set-Cookie": "(?:exp_last_activity|exp_tracker|ci_(?:session|(csrf_token)))\\;version:\\1?2+:"
            },
            "html": "<input[^>]+name=\"ci_csrf_token\"\\;version:2+",
            "icon": "CodeIgniter.png",
            "implies": "PHP",
            "website": "codeigniter.com"
        },
        "CodeMirror": {
            "cats": [
                19
            ],
            "env": "^CodeMirror$",
            "icon": "CodeMirror.png",
            "website": "codemirror.net"
        },
        "Commerce Server": {
            "cats": [
                6
            ],
            "headers": {
                "COMMERCE-SERVER-SOFTWARE": ""
            },
            "icon": "Commerce Server.png",
            "implies": "Microsoft ASP.NET",
            "website": "commerceserver.net"
        },
        "CompaqHTTPServer": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "CompaqHTTPServer\\/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "HP.svg",
            "website": "www.hp.com"
        },
        "Concrete5": {
            "cats": [
                1
            ],
            "env": "^CCM_IMAGE_PATH$",
            "icon": "Concrete5.png",
            "implies": "PHP",
            "meta": {
                "generator": "concrete5 - ([\\d.ab]+)\\;version:\\1"
            },
            "script": "concrete/js/",
            "website": "concrete5.org"
        },
        "Connect": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "^Connect$"
            },
            "icon": "Connect.png",
            "implies": "Node.js",
            "website": "www.senchalabs.org/connect"
        },
        "Contao": {
            "cats": [
                1
            ],
            "html": [
                "<!--[^>]+powered by (?:TYPOlight|Contao)[^>]*-->",
                "<link[^>]+(?:typolight|contao)\\.css"
            ],
            "icon": "Contao.png",
            "implies": "PHP",
            "meta": {
                "generator": "^Contao Open Source CMS$"
            },
            "website": "contao.org"
        },
        "Contenido": {
            "cats": [
                1
            ],
            "icon": "Contenido.png",
            "implies": "PHP",
            "meta": {
                "generator": "Contenido ([\\d.]+)\\;version:\\1"
            },
            "website": "contenido.org/en"
        },
        "Contens": {
            "cats": [
                1
            ],
            "icon": "Contens.png",
            "implies": [
                "Java",
                "CFML"
            ],
            "meta": {
                "generator": "Contensis CMS Version ([\\d.]+)\\;version:\\1"
            },
            "website": "www.contens.com/en/pub/index.cfm"
        },
        "ContentBox": {
            "cats": [
                1,
                11
            ],
            "icon": "ContentBox.png",
            "implies": "Adobe ColdFusion",
            "meta": {
                "generator": "ContentBox powered by ColdBox"
            },
            "website": "www.gocontentbox.org"
        },
        "ConversionLab": {
            "cats": [
                10
            ],
            "icon": "ConversionLab.png",
            "script": "conversionlab\\.trackset\\.com/track/tsend\\.js",
            "website": "www.trackset.it/conversionlab"
        },
        "Coppermine": {
            "cats": [
                7
            ],
            "html": "<!--Coppermine Photo Gallery ([\\d.]+)\\;version:\\1",
            "icon": "Coppermine.png",
            "implies": "PHP",
            "website": "coppermine-gallery.net"
        },
        "Cosmoshop": {
            "cats": [
                6
            ],
            "icon": "Cosmoshop.png",
            "script": "cosmoshop_functions\\.js",
            "website": "cosmoshop.de"
        },
        "Cotonti": {
            "cats": [
                1
            ],
            "icon": "Cotonti.png",
            "implies": "PHP",
            "meta": {
                "generator": "Cotonti"
            },
            "website": "www.cotonti.com"
        },
        "CouchDB": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "CouchDB/([\\d.]+)\\;version:\\1"
            },
            "icon": "CouchDB.png",
            "website": "couchdb.apache.org"
        },
        "Cowboy": {
            "cats": [
                18,
                22
            ],
            "headers": {
                "Server": "Cowboy"
            },
            "icon": "Cowboy.png",
            "implies": "Erlang",
            "website": "ninenines.eu"
        },
        "CppCMS": {
            "cats": [
                1
            ],
            "headers": {
                "X-Powered-By": "CppCMS/([\\d.]+)\\;version:\\1"
            },
            "icon": "CppCMS.png",
            "implies": "C++",
            "website": "cppcms.com"
        },
        "Craft CMS": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "CraftSessionId=",
                "X-Powered-By": "Craft CMS"
            },
            "icon": "Craft CMS.png",
            "implies": "PHP",
            "website": "buildwithcraft.com"
        },
        "Crazy Egg": {
            "cats": [
                10
            ],
            "env": "^CE2$",
            "icon": "Crazy Egg.png",
            "script": "cetrk\\.com/pages/scripts/\\d+/\\d+\\.js",
            "website": "crazyegg.com"
        },
        "Criteo": {
            "cats": [
                36
            ],
            "env": "^criteo",
            "icon": "Criteo.svg",
            "script": "[^/]*//(?:cas\\.criteo\\.com|(?:[^/]\\.)?criteo\\.net)/",
            "website": "criteo.com"
        },
        "Cross Pixel": {
            "cats": [
                10
            ],
            "env": "^crsspxl$",
            "icon": "Cross Pixel.png",
            "script": "tag\\.crsspxl\\.com/s1\\.js",
            "website": "datadesk.crsspxl.com"
        },
        "CubeCart": {
            "cats": [
                6
            ],
            "html": "(?:Powered by <a href=[^>]+cubecart\\.com|<p[^>]+>Powered by CubeCart)",
            "icon": "CubeCart.png",
            "implies": "PHP",
            "meta": {
                "generator": "cubecart"
            },
            "website": "www.cubecart.com"
        },
        "Cufon": {
            "cats": [
                17
            ],
            "env": "^Cufon$",
            "icon": "Cufon.png",
            "script": "cufon-yui\\.js",
            "website": "cufon.shoqolate.com"
        },
        "D3": {
            "cats": [
                25
            ],
            "env": "^d3$",
            "icon": "D3.png",
            "script": "d3(?:\\. v\\d+)?(?:\\.min)?\\.js",
            "website": "d3js.org"
        },
        "DHTMLX": {
            "cats": [
                12
            ],
            "icon": "DHTMLX.png",
            "script": "dhtmlxcommon\\.js",
            "website": "dhtmlx.com"
        },
        "DM Polopoly": {
            "cats": [
                1
            ],
            "html": "<(?:link [^>]*href|img [^>]*src)=\"/polopoly_fs/",
            "icon": "DM Polopoly.png",
            "implies": "Java",
            "website": "www.atex.com/products/dm-polopoly"
        },
        "DNN": {
            "cats": [
                1
            ],
            "env": "^DotNetNuke$",
            "headers": {
                "Cookie": "dnn_IsMobile=",
                "DNNOutputCache": "",
                "Set-Cookie": "DotNetNukeAnonymous=",
                "X-Compressed-By": "DotNetNuke"
            },
            "html": [
                "<!-- by DotNetNuke Corporation",
                "<!-- DNN Platform"
            ],
            "icon": "DNN.png",
            "implies": "Microsoft ASP.NET",
            "meta": {
                "generator": "DotNetNuke"
            },
            "script": [
                "/js/dnncore\\.js",
                "/js/dnn\\.js"
            ],
            "website": "dnnsoftware.com"
        },
        "DTG": {
            "cats": [
                1
            ],
            "html": [
                "<a[^>]+Site Powered by DTG"
            ],
            "icon": "DTG.png",
            "implies": "Mono.net",
            "website": "www.dtg.nl"
        },
        "Dancer": {
            "cats": [
                18
            ],
            "headers": {
                "Server": "Perl Dancer ([\\d.]+)\\;version:\\1",
                "X-Powered-By": "Perl Dancer ([\\d.]+)\\;version:\\1"
            },
            "icon": "Dancer.png",
            "implies": "Perl",
            "website": "perldancer.org"
        },
        "Danneo CMS": {
            "cats": [
                1
            ],
            "headers": {
                "X-Powered-By": "CMS Danneo ([\\d.]+)\\;version:\\1"
            },
            "icon": "Danneo CMS.png",
            "implies": [
                "Apache",
                "PHP"
            ],
            "meta": {
                "generator": "Danneo CMS ([\\d.]+)\\;version:\\1"
            },
            "website": "danneo.com"
        },
        "Darwin": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "Darwin",
                "X-Powered-By": "Darwin"
            },
            "icon": "Darwin.png",
            "website": "opensource.apple.com"
        },
        "DataLife Engine": {
            "cats": [
                1
            ],
            "env": "^dle_root$",
            "icon": "DataLife Engine.png",
            "implies": [
                "PHP",
                "Apache"
            ],
            "meta": {
                "generator": "DataLife Engine"
            },
            "website": "dle-news.ru"
        },
        "DataTables": {
            "cats": [
                12
            ],
            "icon": "DataTables.png",
            "implies": "jQuery",
            "script": "dataTables.*\\.js",
            "website": "datatables.net"
        },
        "David Webbox": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "David-WebBox/([\\d.a]+ \\(\\d+\\))\\;version:\\1"
            },
            "icon": "David Webbox.png",
            "website": "www.tobit.com"
        },
        "Debian": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "Debian",
                "X-Powered-By": "(?:Debian|dotdeb|(sarge|etch|lenny|squeeze|wheezy|jessie))\\;version:\\1"
            },
            "icon": "Debian.png",
            "website": "debian.org"
        },
        "Decorum": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "DECORUM(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "???"
        },
        "DedeCMS": {
            "cats": [
                1
            ],
            "env": "^DedeContainer",
            "icon": "DedeCMS.png",
            "implies": "PHP",
            "script": "dedeajax",
            "website": "dedecms.com"
        },
        "Dell": {
            "cats": [
                40
            ],
            "icon": "Dell.png",
            "website": "dell.com"
        },
        "Demandware": {
            "cats": [
                6
            ],
            "env": "^dwAnalytics$",
            "headers": {
                "Server": "Demandware eCommerce Server"
            },
            "html": "<[^>]+demandware\\.edgesuite",
            "icon": "Demandware.png",
            "website": "demandware.com"
        },
        "Deployd": {
            "cats": [
                12
            ],
            "env": "^dpd$",
            "icon": "Deployd.png",
            "script": "dpd\\.js",
            "website": "deployd.com"
        },
        "DirectAdmin": {
            "cats": [
                9
            ],
            "headers": {
                "Server": "DirectAdmin Daemon v([\\d.]+)\\;version:\\1"
            },
            "html": "<a[^>]+>DirectAdmin</a> Web Control Panel",
            "icon": "DirectAdmin.png",
            "implies": [
                "PHP",
                "Apache"
            ],
            "website": "www.directadmin.com"
        },
        "Discourse": {
            "cats": [
                2
            ],
            "env": "Discourse",
            "icon": "Discourse.png",
            "implies": [
                "Ruby on Rails"
            ],
            "meta": {
                "generator": "Discourse(?: ?/?([\\d.]+\\d))?\\;version:\\1"
            },
            "website": "discourse.org"
        },
        "Discuz! X": {
            "cats": [
                2
            ],
            "env": [
                "^discuz_uid$",
                "^DISCUZCODE$"
            ],
            "icon": "Discuz! X.png",
            "implies": "PHP",
            "meta": {
                "generator": "Discuz! X([\\d\\.]+)?\\;version:\\1"
            },
            "website": "discuz.com"
        },
        "Disqus": {
            "cats": [
                15
            ],
            "env": "^DISQUS",
            "html": "<div[^>]+id=\"disqus_thread\"",
            "icon": "Disqus.svg",
            "script": "disqus_url",
            "website": "disqus.com"
        },
        "Django": {
            "cats": [
                18
            ],
            "env": "^__admin_media_prefix__",
            "html": "(?:powered by <a[^>]+>Django ?([\\d.]+)?|<input[^>]*name=[\"']csrfmiddlewaretoken[\"'][^>]*>)\\;version:\\1",
            "icon": "Django.png",
            "implies": "Python",
            "website": "djangoproject.com"
        },
        "Django CMS": {
            "cats": [
                1
            ],
            "icon": "Django CMS.png",
            "implies": "Django",
            "website": "django-cms.org"
        },
        "Dojo": {
            "cats": [
                12
            ],
            "env": "^dojo$",
            "icon": "Dojo.png",
            "script": "([\\d.]+)/dojo/dojo(?:\\.xd)?\\.js\\;version:\\1",
            "website": "dojotoolkit.org"
        },
        "Dokeos": {
            "cats": [
                21
            ],
            "headers": {
                "X-Powered-By": "Dokeos"
            },
            "html": "(?:Portal <a[^>]+>Dokeos|@import \"[^\"]+dokeos_blue)",
            "icon": "Dokeos.png",
            "implies": [
                "PHP",
                "Xajax",
                "jQuery",
                "CKEditor"
            ],
            "meta": {
                "generator": "Dokeos"
            },
            "website": "dokeos.com"
        },
        "DokuWiki": {
            "cats": [
                8
            ],
            "headers": {
                "Set-Cookie": "DokuWiki="
            },
            "icon": "DokuWiki.png",
            "implies": "PHP",
            "meta": {
                "generator": "DokuWiki( Release [\\-\\d]+)?\\;version:\\1"
            },
            "website": "www.dokuwiki.org"
        },
        "Dotclear": {
            "cats": [
                1
            ],
            "icon": "Dotclear.png",
            "implies": "PHP",
            "website": "dotclear.org"
        },
        "DoubleClick Ad Exchange (AdX)": {
            "cats": [
                36
            ],
            "icon": "DoubleClick.svg",
            "script": [
                "googlesyndication\\.com/pagead/show_ads\\.js",
                "tpc\\.googlesyndication\\.com/safeframe",
                "googlesyndication\\.com.*abg\\.js"
            ],
            "website": "www.doubleclickbygoogle.com/solutions/digital-marketing/ad-exchange/"
        },
        "DoubleClick Campaign Manager (DCM)": {
            "cats": [
                36
            ],
            "icon": "DoubleClick.svg",
            "script": "2mdn\\.net",
            "website": "www.doubleclickbygoogle.com/solutions/digital-marketing/campaign-manager/"
        },
        "DoubleClick Floodlight": {
            "cats": [
                36
            ],
            "icon": "DoubleClick.svg",
            "script": "https?://fls.doubleclick.net",
            "website": "support.google.com/ds/answer/6029713?hl=en"
        },
        "DoubleClick for Publishers (DFP)": {
            "cats": [
                36
            ],
            "icon": "DoubleClick.svg",
            "script": "googletagservices\\.com/tag/js/gpt(?:_mobile)?\\.js",
            "website": "www.google.com/dfp"
        },
        "Doxygen": {
            "cats": [
                4
            ],
            "html": "(?:<!-- Generated by Doxygen ([\\d.]+)|<link[^>]+doxygen\\.css)\\;version:\\1",
            "icon": "Doxygen.png",
            "meta": {
                "generator": "Doxygen ([\\d.]+)\\;version:\\1"
            },
            "website": "www.stack.nl/~dimitri/doxygen/"
        },
        "DreamWeaver": {
            "cats": [
                20
            ],
            "html": "(?:<!--[^>]*(?:InstanceBeginEditable|Dreamweaver([^>]+)target|DWLayoutDefaultTable)|function MM_preloadImages\\(\\) \\{)\\;version:\\1",
            "icon": "DreamWeaver.png",
            "website": "www.adobe.com/products/dreamweaver"
        },
        "Drupal": {
            "cats": [
                1
            ],
            "env": "^Drupal$",
            "headers": {
                "Expires": "19 Nov 1978",
                "X-Drupal-Cache": "",
                "X-Generator": "Drupal(?:\\s([\\d.]+))?\\;version:\\1"
            },
            "html": "<(?:link|style)[^>]+sites/(?:default|all)/(?:themes|modules)/",
            "icon": "Drupal.png",
            "implies": "PHP",
            "meta": {
                "generator": "Drupal(?:\\s([\\d.]+))?\\;version:\\1"
            },
            "script": "drupal\\.js",
            "website": "drupal.org"
        },
        "Drupal Commerce": {
            "cats": [
                6
            ],
            "html": "<[^>]+(?:id=\"block[_-]commerce[_-]cart[_-]cart|class=\"commerce[_-]product[_-]field)",
            "icon": "Drupal Commerce.png",
            "implies": "Drupal",
            "website": "drupalcommerce.org"
        },
        "Dynamicweb": {
            "cats": [
                1,
                6,
                10
            ],
            "headers": {
                "Set-Cookie": "Dynamicweb="
            },
            "icon": "Dynamicweb.png",
            "implies": "Microsoft ASP.NET",
            "meta": {
                "generator": "Dynamicweb ([\\d.]+)\\;version:\\1"
            },
            "website": "www.dynamicweb.dk"
        },
        "Dynatrace": {
            "cats": [
                10
            ],
            "icon": "Dynatrace.png",
            "script": "dtagent.*\\.js",
            "website": "dynatrace.com"
        },
        "E-Merchant": {
            "cats": [
                6
            ],
            "icon": "E-Merchant.png",
            "script": "cdn\\.e-merchant\\.com",
            "website": "e-merchant.com"
        },
        "ELOG": {
            "cats": [
                19
            ],
            "html": "<title>ELOG Logbook Selection</title>",
            "icon": "ELOG.png",
            "website": "midas.psi.ch/elog"
        },
        "ELOG HTTP": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "ELOG HTTP( \\d[\\-\\d\\.]+)?\\;version:\\1"
            },
            "icon": "ELOG HTTP.png",
            "implies": "ELOG",
            "website": "midas.psi.ch/elog"
        },
        "EPages": {
            "cats": [
                6
            ],
            "headers": {
                "X-Powered-By": "epages 6"
            },
            "html": "<div class=\"BoxContainer\">",
            "icon": "epages.png",
            "website": "www.epages.com/"
        },
        "EPiServer": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "EPi(?:Trace|Server)[^;]*="
            },
            "icon": "EPiServer.png",
            "implies": "Microsoft ASP.NET",
            "meta": {
                "generator": "EPiServer"
            },
            "website": "episerver.com"
        },
        "EPrints": {
            "cats": [
                19
            ],
            "env": "^EPJS_menu_template$",
            "icon": "EPrints.png",
            "implies": "Perl",
            "meta": {
                "generator": "EPrints ([\\d.]+)\\;version:\\1"
            },
            "website": "www.eprints.org"
        },
        "ESERV-10": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "ESERV-10(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "ESERV-10.png",
            "website": "www.violasystems.com"
        },
        "EWS-NIC4": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "EWS-NIC4(?:\\/([\\d\\.a-z]+))?\\;version:\\1"
            },
            "icon": "EWS-NIC4.png",
            "implies": "Dell",
            "website": "dell.com"
        },
        "EdgeCast": {
            "cats": [
                31
            ],
            "headers": {
                "Server": "^EC(?:S|Acc)"
            },
            "icon": "EdgeCast.png",
            "url": "https?://(?:[^/]+\\.)?edgecastcdn\\.net/",
            "website": "www.edgecast.com"
        },
        "Elcodi": {
            "cats": [
                6
            ],
            "headers": {
                "X-Elcodi": ""
            },
            "icon": "Elcodi.png",
            "implies": [
                "PHP",
                "Symfony"
            ],
            "website": "elcodi.io"
        },
        "Eleanor CMS": {
            "cats": [
                1
            ],
            "icon": "Eleanor CMS.png",
            "implies": "PHP",
            "meta": {
                "generator": "Eleanor"
            },
            "website": "eleanor-cms.ru"
        },
        "Elm": {
            "cats": [
                27,
                12
            ],
            "env": "^Elm$",
            "icon": "Elm.png",
            "website": "elm-lang.org"
        },
        "Eloqua": {
            "cats": [
                32
            ],
            "env": "^elq(?:SiteID|Load|CurESite)$",
            "icon": "Oracle.png",
            "script": "elqCfg\\.js",
            "website": "eloqua.com"
        },
        "EmbedThis Appweb": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Mbedthis-Appweb(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "EmbedThis Appweb.png",
            "website": "embedthis.com/appweb"
        },
        "Embedthis-http": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Embedthis-http(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Embedthis-http.png",
            "website": "github.com/embedthis/http"
        },
        "Ember.js": {
            "cats": [
                12
            ],
            "env": "^Ember$",
            "icon": "Ember.js.png",
            "implies": "Handlebars",
            "website": "emberjs.com"
        },
        "Enyo": {
            "cats": [
                12,
                26
            ],
            "env": "^enyo$",
            "icon": "Enyo.png",
            "script": "\benyo\\.js",
            "website": "enyojs.com"
        },
        "Epoch": {
            "cats": [
                25
            ],
            "html": "<link[^>]+?href=\"[^\"]+epoch(?:\\.min)?\\.css",
            "icon": "default.png",
            "implies": "D3",
            "script": "epoch(?:\\.min)?\\.js",
            "website": "fastly.github.io/epoch"
        },
        "Epom": {
            "cats": [
                36
            ],
            "env": "^Epom",
            "icon": "Epom.png",
            "url": "^https?://(?:[^/]+\\.)?ad(?:op)?shost1\\.com/",
            "website": "epom.com"
        },
        "Erlang": {
            "cats": [
                27
            ],
            "headers": {
                "Server": "Erlang( OTP/(?:[\\-\\d\\.ABR]+))?\\;version:\\1"
            },
            "icon": "Erlang.png",
            "website": "www.erlang.org"
        },
        "Exagon Concept": {
            "cats": [
                1
            ],
            "headers": {
                "Server": "Exagon Server"
            },
            "icon": "ExagonConcept.svg",
            "website": "www.exagon-concept.com"
        },
        "Exhibit": {
            "cats": [
                25
            ],
            "env": "^Exhibit$",
            "icon": "Exhibit.png",
            "script": "exhibit.*\\.js",
            "website": "simile-widgets.org/exhibit/"
        },
        "Express": {
            "cats": [
                18,
                22
            ],
            "headers": {
                "X-Powered-By": "^Express$"
            },
            "icon": "Express.png",
            "implies": "Node.js",
            "website": "expressjs.com"
        },
        "ExpressionEngine": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "(?:exp_last_activity|exp_tracker)"
            },
            "icon": "ExpressionEngine.png",
            "implies": "PHP",
            "website": "expressionengine.com"
        },
        "ExtJS": {
            "cats": [
                12
            ],
            "env": "^Ext$",
            "icon": "ExtJS.png",
            "script": "ext-base\\.js",
            "website": "www.extjs.com"
        },
        "FAST ESP": {
            "cats": [
                29
            ],
            "html": "<form[^>]+id=\"fastsearch\"",
            "icon": "FAST ESP.png",
            "website": "microsoft.com/enterprisesearch"
        },
        "FAST Search for SharePoint": {
            "cats": [
                29
            ],
            "html": "<input[^>]+ name=\"ParametricSearch",
            "icon": "FAST Search for SharePoint.png",
            "implies": [
                "Microsoft SharePoint",
                "Microsoft ASP.NET"
            ],
            "url": "Pages/SearchResults\\.aspx\\?k=",
            "website": "sharepoint.microsoft.com/en-us/product/capabilities/search/Pages/Fast-Search.aspx"
        },
        "FWP": {
            "cats": [
                6
            ],
            "html": "<!--\\s+FwP Systems",
            "icon": "FWP.png",
            "meta": {
                "generator": "FWP Shop"
            },
            "website": "fwpshop.org"
        },
        "Fact Finder": {
            "cats": [
                29
            ],
            "html": "<!-- Factfinder",
            "icon": "Fact Finder.png",
            "script": "Suggest\\.ff",
            "url": "(?:/ViewParametricSearch|ffsuggest\\.[a-z]htm)",
            "website": "fact-finder.com"
        },
        "Fat-Free Framework": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "Fat-Free Framework"
            },
            "icon": "Fat-Free Framework.png",
            "implies": "PHP",
            "website": "fatfreeframework.com"
        },
        "Fedora": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "Fedora"
            },
            "icon": "Fedora.png",
            "website": "fedoraproject.org"
        },
        "Firebase": {
            "cats": [
                34
            ],
            "icon": "Firebase.png",
            "script": "firebase.*\\.js",
            "website": "firebase.com"
        },
        "Fireblade": {
            "cats": [
                31
            ],
            "headers": {
                "Server": "fbs"
            },
            "icon": "Fireblade.png",
            "website": "fireblade.com"
        },
        "FlashCom": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "FlashCom/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "???"
        },
        "Flask": {
            "cats": [
                18,
                22
            ],
            "headers": {
                "Server": "Werkzeug/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "Flask.png",
            "implies": "Python",
            "website": "flask.pocoo.org"
        },
        "FlexCMP": {
            "cats": [
                1
            ],
            "headers": {
                "X-Flex-Lang": "",
                "X-Powered-By": "FlexCMP.+\\[v\\. ([\\d.]+)\\;version:\\1"
            },
            "html": "<!--[^>]+FlexCMP[^>v]+v\\. ([\\d.]+)\\;version:\\1",
            "icon": "FlexCMP.png",
            "meta": {
                "generator": "FlexCMP"
            },
            "website": "www.flexcmp.com/cms/home"
        },
        "FluxBB": {
            "cats": [
                2
            ],
            "html": "Powered by (?:<strong>)?<a href=\"[^>]+fluxbb",
            "icon": "FluxBB.png",
            "website": "fluxbb.org"
        },
        "Flyspray": {
            "cats": [
                13
            ],
            "headers": {
                "Set-Cookie": "flyspray_project="
            },
            "html": "(?:<a[^>]+>Powered by Flyspray|<map id=\"projectsearchform)",
            "icon": "Flyspray.png",
            "website": "flyspray.org"
        },
        "Font Awesome": {
            "cats": [
                17
            ],
            "html": "<link[^>]* href=[^>]+font-awesome(?:\\.min)?\\.css",
            "icon": "Font Awesome.png",
            "website": "fontawesome.io"
        },
        "Fortune3": {
            "cats": [
                6
            ],
            "html": "(?:<link [^>]*href=\"[^\\/]*\\/\\/www\\.fortune3\\.com\\/[^\"]*siterate\\/rate\\.css|Powered by <a [^>]*href=\"[^\"]+fortune3\\.com)",
            "icon": "Fortune3.png",
            "script": "cartjs\\.php\\?(?:.*&)?s=[^&]*myfortune3cart\\.com",
            "website": "fortune3.com"
        },
        "FreeBSD": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "FreeBSD(?: ([\\d.]+))?\\;version:\\1"
            },
            "icon": "FreeBSD.png",
            "website": "freebsd.org"
        },
        "FreeTextBox": {
            "cats": [
                24
            ],
            "env": "^FTB_",
            "html": "/<!--\\s*\\*\\s*FreeTextBox v\\d+ \\(([.\\d]+)(?:(?:.|\n)+?<!--\\s*\\*\\s*License Type: (Distribution|Professional)License)?/i\\;version:\\1 \\2",
            "icon": "FreeTextBox.png",
            "implies": "Microsoft ASP.NET",
            "website": "freetextbox.com"
        },
        "FrontPage": {
            "cats": [
                20
            ],
            "html": "<html[^>]+urn:schemas-microsoft-com:office:office",
            "icon": "FrontPage.png",
            "meta": {
                "generator": "Microsoft FrontPage(?:\\s((?:Express )?[\\d.]+))?\\;version:\\1"
            },
            "website": "office.microsoft.com/frontpage"
        },
        "Fusion Ads": {
            "cats": [
                36
            ],
            "env": "^_fusion",
            "icon": "Fusion Ads.png",
            "script": "^[^\\/]*//[ac]dn\\.fusionads\\.net/(?:api/([\\d.]+)/)?\\;version:\\1",
            "website": "fusionads.net"
        },
        "G-WAN": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "G-WAN"
            },
            "icon": "G-WAN.png",
            "website": "gwan.com"
        },
        "GX WebManager": {
            "cats": [
                1
            ],
            "html": "<!--\\s+Powered by GX",
            "icon": "GX WebManager.png",
            "meta": {
                "generator": "GX WebManager(?: ([\\d.]+))?\\;version:\\1"
            },
            "website": "www.gxsoftware.com/en/products/web-content-management.htm"
        },
        "Gallery": {
            "cats": [
                7
            ],
            "env": "^galleryAuthToken$",
            "html": "<div id=\"gsNavBar\" class=\"gcBorder1\">",
            "icon": "Gallery.png",
            "website": "gallery.menalto.com"
        },
        "Gambio": {
            "cats": [
                6
            ],
            "env": "^gm_session_id$",
            "html": "(?:<link[^>]* href=\"templates/gambio/|<a[^>]content\\.php\\?coID=\\d|<!-- gambio eof -->|<!--[\\s=]+Shopsoftware by Gambio GmbH \\(c\\))",
            "icon": "Gambio.png",
            "implies": "PHP",
            "script": "gm_javascript\\.js\\.php",
            "website": "gambio.de"
        },
        "Gauges": {
            "cats": [
                10
            ],
            "env": "^_gauges$",
            "headers": {
                "Set-Cookie": "_gauges_[^;]+="
            },
            "icon": "Gauges.png",
            "website": "get.gaug.es"
        },
        "Gentoo": {
            "cats": [
                28
            ],
            "headers": {
                "X-Powered-By": "gentoo"
            },
            "icon": "Gentoo.png",
            "website": "www.gentoo.org"
        },
        "Get Satisfaction": {
            "cats": [
                13
            ],
            "env": "^GSFN",
            "icon": "Get Satisfaction.png",
            "website": "getsatisfaction.com"
        },
        "GetSimple CMS": {
            "cats": [
                1
            ],
            "icon": "GetSimple CMS.png",
            "implies": "PHP",
            "meta": {
                "generator": "GetSimple"
            },
            "website": "get-simple.info"
        },
        "Ghost": {
            "cats": [
                11
            ],
            "headers": {
                "X-Ghost-Cache-Status": ""
            },
            "icon": "Ghost.png",
            "meta": {
                "generator": "Ghost(?:\\s([\\d.]+))?\\;version:\\1"
            },
            "website": "ghost.org"
        },
        "GitBook": {
            "cats": [
                4
            ],
            "icon": "GitBook.png",
            "meta": {
                "generator": "GitBook(?:.([\\d.]+))?\\;version:\\1"
            },
            "website": "gitbook.io"
        },
        "GitLab": {
            "cats": [
                13,
                47
            ],
            "headers": {
                "Set-cookie": "_gitlab_session"
            },
            "icon": "GitLab.svg",
            "implies": [
                "Ruby",
                "Ruby on Rails"
            ],
            "website": "about.gitlab.com"
        },
        "GitLab CI": {
            "cats": [
                44,
                47
            ],
            "icon": "GitLab CI.png",
            "implies": [
                "Ruby",
                "Ruby on Rails"
            ],
            "meta": {
                "description": "GitLab Continuous Integration"
            },
            "website": "about.gitlab.com/gitlab-ci"
        },
        "GlassFish": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "GlassFish(?: Server)?(?: Open Source Edition)?(?: ?/?([\\d.]+))?\\;version:\\1"
            },
            "icon": "GlassFish.png",
            "implies": [
                "Java"
            ],
            "website": "glassfish.java.net"
        },
        "Glyphicons": {
            "cats": [
                17
            ],
            "html": "(?:<link[^>]* href=[^>]+glyphicons(?:\\.min)?\\.css|<img[^>]* src=[^>]+glyphicons)",
            "icon": "Glyphicons.png",
            "website": "glyphicons.com"
        },
        "GoAhead": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "GoAhead"
            },
            "icon": "GoAhead.png",
            "website": "embedthis.com/products/goahead/index.html"
        },
        "GoStats": {
            "cats": [
                10
            ],
            "env": "^_go(?:stats|_track)",
            "icon": "GoStats.png",
            "website": "gostats.com"
        },
        "Google AdSense": {
            "cats": [
                36
            ],
            "env": [
                "^google_ad_",
                "^__google_ad_",
                "^Goog_AdSense_"
            ],
            "icon": "Google AdSense.svg",
            "script": [
                "googlesyndication\\.com/",
                "ad\\.ca\\.doubleclick\\.net",
                "2mdn\\.net",
                "ad\\.ca\\.doubleclick\\.net"
            ],
            "website": "google.com/adsense"
        },
        "Google Analytics": {
            "cats": [
                10
            ],
            "env": "^gaGlobal$",
            "headers": {
                "Set-Cookie": "__utma"
            },
            "icon": "Google Analytics.svg",
            "script": "^https?://[^\\/]+\\.google-analytics\\.com\\/(?:ga|urchin|(analytics))\\.js\\;version:\\1?UA:",
            "website": "google.com/analytics"
        },
        "Google App Engine": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Google Frontend"
            },
            "icon": "Google App Engine.png",
            "website": "code.google.com/appengine"
        },
        "Google Charts": {
            "cats": [
                25
            ],
            "env": "^__g(?:oogleVisualizationAbstractRendererElementsCount|vizguard)__$",
            "icon": "Google Charts.png",
            "website": "developers.google.com/chart/"
        },
        "Google Code Prettify": {
            "cats": [
                19
            ],
            "env": "^prettyPrint$",
            "icon": "Google Code Prettify.png",
            "website": "code.google.com/p/google-code-prettify"
        },
        "Google Font API": {
            "cats": [
                17
            ],
            "env": "^WebFonts$",
            "html": "<link[^>]* href=[^>]+fonts\\.(?:googleapis|google)\\.com",
            "icon": "Google Font API.png",
            "script": "googleapis\\.com/.+webfont",
            "website": "google.com/fonts"
        },
        "Google Maps": {
            "cats": [
                35
            ],
            "icon": "Google Maps.png",
            "script": [
                "(?:maps\\.google\\.com/maps\\?file=api(?:&v=([\\d.]+))?|maps\\.google\\.com/maps/api/staticmap)\\;version:API v\\1",
                "//maps.googleapis.com/maps/api/js"
            ],
            "website": "maps.google.com"
        },
        "Google PageSpeed": {
            "cats": [
                23,
                33
            ],
            "headers": {
                "X-Mod-Pagespeed": "([\\d.]+)\\;version:\\1",
                "X-Page-Speed": "(.+)\\;version:\\1"
            },
            "icon": "Google PageSpeed.png",
            "website": "developers.google.com/speed/pagespeed/mod"
        },
        "Google Sites": {
            "cats": [
                1
            ],
            "icon": "Google Sites.png",
            "url": "sites\\.google\\.com",
            "website": "sites.google.com"
        },
        "Google Tag Manager": {
            "cats": [
                42
            ],
            "env": "^googletag$",
            "html": "googletagmanager\\.com/ns\\.html[^>]+></iframe>",
            "icon": "Google Tag Manager.png",
            "website": "www.google.com/tagmanager"
        },
        "Google Wallet": {
            "cats": [
                41
            ],
            "icon": "Google Wallet.png",
            "script": [
                "checkout\\.google\\.com",
                "wallet\\.google\\.com"
            ],
            "website": "wallet.google.com"
        },
        "Google Web Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "gws"
            },
            "icon": "Google Web Server.png",
            "website": "en.wikipedia.org/wiki/Google_Web_Server"
        },
        "Google Web Toolkit": {
            "cats": [
                18
            ],
            "env": "^__gwt_",
            "icon": "Google Web Toolkit.png",
            "implies": "Java",
            "meta": {
                "gwt:property": ""
            },
            "website": "developers.google.com/web-toolkit"
        },
        "Graffiti CMS": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "graffitibot[^;]="
            },
            "icon": "Graffiti CMS.png",
            "meta": {
                "generator": "Graffiti CMS ([^\"]+)\\;version:\\1"
            },
            "script": "/graffiti\\.js",
            "website": "graffiticms.codeplex.com"
        },
        "Grandstream": {
            "cats": [
                22,
                39
            ],
            "headers": {
                "Server": "Grandstream\\/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "Grandstream.png",
            "website": "www.grandstream.com"
        },
        "Grav": {
            "cats": [
                1
            ],
            "icon": "Grav.png",
            "implies": [
                "PHP"
            ],
            "meta": {
                "generator": "GravCMS(?:\\s([\\d.]+))?\\;version:\\1"
            },
            "website": "getgrav.org"
        },
        "Gravatar": {
            "cats": [
                19
            ],
            "env": "^Gravatar$",
            "html": "<[^>]+gravatar\\.com/avatar/",
            "icon": "Gravatar.png",
            "website": "gravatar.com"
        },
        "Gravity Insights": {
            "cats": [
                10
            ],
            "env": "^GravityInsights$",
            "icon": "Gravity Insights.png",
            "website": "insights.gravity.com"
        },
        "Green Valley CMS": {
            "cats": [
                1
            ],
            "html": "<img[^>]+/dsresource\\?objectid=",
            "icon": "Green Valley CMS.png",
            "meta": {
                "DC.identifier": "/content\\.jsp\\?objectid="
            },
            "website": "www.greenvalley.nl/Public/Producten/Content_Management/CMS"
        },
        "HERE": {
            "cats": [
                35
            ],
            "icon": "HERE.png",
            "script": "https?://js\\.cit\\.api\\.here\\.com/se/([\\d.]+)\\/\\;version:\\1",
            "website": "developer.here.com"
        },
        "HHVM": {
            "cats": [
                22
            ],
            "headers": {
                "X-Powered-By": "HHVM/?([\\d.]+)?\\;version:\\1"
            },
            "icon": "HHVM.png",
            "implies": "PHP",
            "website": "hhvm.com"
        },
        "HP": {
            "cats": [
                40
            ],
            "icon": "HP.svg",
            "website": "hp.com"
        },
        "HP ChaiServer": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "HP-Chai(?:Server|SOE)(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "HP.svg",
            "implies": [
                "HP"
            ],
            "website": "hp.com"
        },
        "HP Compact Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "HP_Compact_Server(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "HP.svg",
            "website": "hp.com"
        },
        "HP ProCurve": {
            "cats": [
                37
            ],
            "icon": "HP.svg",
            "website": "hp.com/networking"
        },
        "HP System Management": {
            "cats": [
                46
            ],
            "headers": {
                "Server": "HP System Management"
            },
            "icon": "HP.svg",
            "website": "hp.com"
        },
        "HP iLO": {
            "cats": [
                22,
                46
            ],
            "headers": {
                "Server": "HP-iLO-Server(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "HP.svg",
            "website": "hp.com"
        },
        "HTTP Kit": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "^http-kit"
            },
            "icon": "default.png",
            "implies": "Java",
            "website": "http-kit.org"
        },
        "HTTP-Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "(?:^|[^-])\bHTTP-Server(?: ?/?V?([\\d.]+))?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "???"
        },
        "HTTP/2": {
            "cats": [
                19
            ],
            "excludes": "SPDY",
            "headers": {
                "X-Firefox-Spdy": "h2"
            },
            "icon": "default.png",
            "website": "http2.github.io"
        },
        "Hammer.js": {
            "cats": [
                12
            ],
            "env": "^Hammer$",
            "icon": "Hammer.js.png",
            "script": "hammer(?:\\.min)?\\.js",
            "website": "hammerjs.github.io"
        },
        "Handlebars": {
            "cats": [
                12
            ],
            "env": "^Handlebars$",
            "html": "<[^>]*type=[^>]text\\/x-handlebars-template",
            "icon": "Handlebars.png",
            "script": "handlebars(?:\\.runtime)?(?:-v([\\d.]+?))?(?:\\.min)?\\.js\\;version:\\1",
            "website": "handlebarsjs.com"
        },
        "Happy ICS Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Happy ICS Server(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "default.png",
            "implies": "OmniTouch 8660 My Teamwork",
            "website": "???"
        },
        "Haskell": {
            "cats": [
                27
            ],
            "icon": "Haskell.png",
            "website": "wiki.haskell.org/Haskell"
        },
        "HeadJS": {
            "cats": [
                12
            ],
            "env": "^head$",
            "html": "<[^>]*data-headjs-load",
            "icon": "HeadJS.png",
            "script": "head\\.(?:core|load)(?:\\.min)?\\.js",
            "website": "headjs.com"
        },
        "Heap": {
            "cats": [
                10
            ],
            "env": "^heap$",
            "icon": "Heap.png",
            "script": "heap-\\d+.js",
            "website": "heapanalytics.com"
        },
        "Hello Bar": {
            "cats": [
                5
            ],
            "env": "^HelloBar$",
            "icon": "Hello Bar.png",
            "script": "hellobar\\.js",
            "website": "hellobar.com"
        },
        "Hiawatha": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Hiawatha v([\\d.]+)\\;version:\\1"
            },
            "icon": "Hiawatha.png",
            "website": "hiawatha-webserver.org"
        },
        "Highcharts": {
            "cats": [
                25
            ],
            "env": "^Highcharts$",
            "html": "<svg[^>]*><desc>Created with Highcharts ([\\d.]*)\\;version:\\1",
            "icon": "Highcharts.png",
            "script": "highcharts.*\\.js",
            "website": "highcharts.com"
        },
        "Highstock": {
            "cats": [
                25
            ],
            "html": "<svg[^>]*><desc>Created with Highstock ([\\d.]*)\\;version:\\1",
            "icon": "Highstock.png",
            "script": "highstock(?:\\-|\\.)?([\\d\\.]*\\d).*\\.js\\;version:\\1",
            "website": "highcharts.com/products/highstock"
        },
        "Hippo": {
            "cats": [
                1
            ],
            "html": "<[^>]+/binaries/(?:[^/]+/)*content/gallery/",
            "icon": "Hippo.png",
            "website": "onehippo.org"
        },
        "Hogan.js": {
            "cats": [
                12
            ],
            "env": "^Hogan$",
            "icon": "Hogan.js.png",
            "script": [
                "hogan-(?:-|\\.)([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
                "([\\d.]+)/hogan(?:\\.min)?\\.js\\;version:\\1"
            ],
            "website": "twitter.github.com/hogan.js"
        },
        "Hotaru CMS": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "hotaru_mobile="
            },
            "icon": "Hotaru CMS.png",
            "meta": {
                "generator": "Hotaru CMS"
            },
            "website": "hotarucms.org"
        },
        "HubSpot": {
            "cats": [
                32
            ],
            "env": "^(?:_hsq|hubspot)$",
            "html": "<!-- Start of Async HubSpot",
            "icon": "HubSpot.png",
            "website": "hubspot.com"
        },
        "Hugo": {
            "cats": [
                1,
                11
            ],
            "icon": "Hugo.png",
            "meta": {
                "generator": "Hugo ([\\d.]+)?\\;version:\\1"
            },
            "website": "gohugo.io"
        },
        "Hybris": {
            "cats": [
                6
            ],
            "headers": {
                "Set-Cookie": "_hybris"
            },
            "html": "<[^>]+(?:/sys_master/|/hybr/|/_ui/desktop/)",
            "icon": "Hybris.png",
            "implies": "Java",
            "website": "hybris.com"
        },
        "IBM Coremetrics": {
            "cats": [
                10
            ],
            "icon": "IBM.svg",
            "script": "cmdatatagutils\\.js",
            "website": "ibm.com/software/marketing-solutions/coremetrics"
        },
        "IBM HTTP Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "IBM_HTTP_Server(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "IBM.svg",
            "website": "ibm.com/software/webservers/httpservers"
        },
        "IBM Tivoli Storage Manager": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "TSM_HTTP(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "IBM.svg",
            "website": "ibm.com"
        },
        "IBM WebSphere Commerce": {
            "cats": [
                6
            ],
            "icon": "IBM.svg",
            "implies": "Java",
            "url": "/wcs/",
            "website": "ibm.com/software/genservers/commerceproductline"
        },
        "IBM WebSphere Portal": {
            "cats": [
                1
            ],
            "headers": {
                "IBM-Web2-Location": "",
                "Itx-Generated-Timestamp": ""
            },
            "icon": "IBM.svg",
            "implies": "Java",
            "url": "/wps/",
            "website": "ibm.com/software/websphere/portal"
        },
        "IIS": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "IIS(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "IIS.png",
            "implies": "Windows Server",
            "website": "www.iis.net"
        },
        "INFOnline": {
            "cats": [
                10
            ],
            "env": [
                "^szmvars$",
                "^iam_data$"
            ],
            "icon": "INFOnline.png",
            "script": "^https?://(?:[^/]+\\.)?i(?:oam|v)wbox\\.de/",
            "website": "infonline.de"
        },
        "IPB": {
            "cats": [
                2
            ],
            "env": "^(?:IPBoard$|ipb_var|ipsSettings)",
            "html": "<link[^>]+ipb_[^>]+\\.css",
            "icon": "IPB.png",
            "script": "jscripts/ips_",
            "website": "www.invisionpower.com"
        },
        "Immutable.js": {
            "cats": [
                12
            ],
            "env": "^Immutable$",
            "icon": "Immutable.js.png",
            "script": "^immutable\\.(?:min\\.)?js$",
            "website": "facebook.github.io/immutable-js/"
        },
        "ImpressCMS": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "ICMSession[^;]+=",
                "X-Powered-By": "ImpressCMS"
            },
            "icon": "ImpressCMS.png",
            "implies": "PHP",
            "meta": {
                "generator": "ImpressCMS"
            },
            "script": "include/linkexternal\\.js",
            "website": "www.impresscms.org"
        },
        "ImpressPages": {
            "cats": [
                1
            ],
            "icon": "ImpressPages.png",
            "implies": "PHP",
            "meta": {
                "generator": "ImpressPages(?: CMS)?( [\\d.]*)\\;version:\\1"
            },
            "website": "impresspages.org"
        },
        "InProces": {
            "cats": [
                1
            ],
            "html": "<!-- CSS InProces Portaal default -->",
            "icon": "InProces.png",
            "script": "brein/inproces/website/websitefuncties\\.js",
            "website": "www.brein.nl/oplossing/product/website"
        },
        "Incapsula": {
            "cats": [
                31
            ],
            "headers": {
                "X-CDN": "Incapsula"
            },
            "icon": "Incapsula.png",
            "website": "www.incapsula.com"
        },
        "Indexhibit": {
            "cats": [
                1
            ],
            "html": "<(?:link|a href) [^>]+ndxz-studio",
            "icon": "default.png",
            "implies": [
                "PHP",
                "Apache",
                "Exhibit"
            ],
            "meta": {
                "generator": "Indexhibit"
            },
            "website": "www.indexhibit.org"
        },
        "Indico": {
            "cats": [
                1
            ],
            "headers": {
                "Set-cookie": "MAKACSESSION"
            },
            "html": "Powered by\\s+(?:CERN )?<a href=\"http://(?:cdsware\\.cern\\.ch/indico/|indico-software\\.org|cern\\.ch/indico)\">(?:CDS )?Indico( [\\d\\.]+)?\\;version:\\1",
            "icon": "Indico.png",
            "website": "indico-software.org"
        },
        "Indy": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Indy(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "indyproject.org"
        },
        "Ink": {
            "cats": [
                18
            ],
            "html": "<link [^>]*href=\"[^\"]+ink(?:\\.min)?\\.css",
            "icon": "Ink.png",
            "script": "ink.*\\.js",
            "website": "ink.sapo.pt"
        },
        "InstantCMS": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "InstantCMS\\[logdate\\]="
            },
            "icon": "InstantCMS.png",
            "meta": {
                "generator": "InstantCMS"
            },
            "website": "www.instantcms.ru"
        },
        "Intel Active Management Technology": {
            "cats": [
                22,
                46
            ],
            "headers": {
                "Server": "Intel\\(R\\) Active Management Technology(?: ([\\d.]+))?\\;version:\\1"
            },
            "icon": "Intel Active Management Technology.png",
            "website": "intel.com"
        },
        "IntenseDebate": {
            "cats": [
                15
            ],
            "icon": "IntenseDebate.png",
            "script": "intensedebate\\.com",
            "website": "intensedebate.com"
        },
        "Intercom": {
            "cats": [
                10
            ],
            "env": "^Intercom$",
            "icon": "Intercom.png",
            "script": "(?:api\\.intercom\\.io/api|static\\.intercomcdn\\.com/intercom\\.v1)",
            "website": "intercom.io"
        },
        "Intershop": {
            "cats": [
                6
            ],
            "icon": "Intershop.png",
            "script": "(?:is-bin|INTERSHOP)",
            "website": "intershop.com"
        },
        "Invenio": {
            "cats": [
                50
            ],
            "headers": {
                "Set-cookie": "INVENIOSESSION"
            },
            "html": "(?:Powered by|System)\\s+(?:CERN )?<a (?:class=\"footer\" )?href=\"http://(?:cdsware\\.cern\\.ch(?:/invenio)?|invenio-software\\.org|cern\\.ch/invenio)(?:/)?\">(?:CDS )?Invenio</a>\\s*v?([\\d\\.]+)?\\;version:\\1",
            "icon": "Invenio.png",
            "website": "invenio-software.org"
        },
        "Ionicons": {
            "cats": [
                17
            ],
            "html": "<link[^>]* href=[^>]+ionicons(?:\\.min)?\\.css",
            "icon": "Ionicons.png",
            "website": "ionicons.com"
        },
        "JAlbum": {
            "cats": [
                7
            ],
            "icon": "JAlbum.png",
            "implies": "Java",
            "meta": {
                "generator": "JAlbum( [\\d.]+)?\\;version:\\1"
            },
            "website": "jalbum.net/en"
        },
        "JBoss Application Server": {
            "cats": [
                22
            ],
            "headers": {
                "X-Powered-By": "JBoss(?:-([\\d.]+))?\\;version:\\1"
            },
            "icon": "JBoss Application Server.png",
            "website": "jboss.org/jbossas.html"
        },
        "JBoss Web": {
            "cats": [
                22
            ],
            "excludes": "Apache Tomcat",
            "headers": {
                "X-Powered-By": "JBossWeb(?:-([\\d.]+))?\\;version:\\1"
            },
            "icon": "JBoss Web.png",
            "implies": "JBoss Application Server",
            "website": "jboss.org/jbossweb"
        },
        "JC-HTTPD": {
            "cats": [
                22
            ],
            "excludes": "Apache",
            "headers": {
                "Server": "JC-HTTPD(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "JC-HTTPD.png",
            "implies": [
                "Canon"
            ],
            "website": "canon.com"
        },
        "JS Charts": {
            "cats": [
                25
            ],
            "env": "^JSChart$",
            "icon": "JS Charts.png",
            "script": "jscharts.*\\.js",
            "website": "www.jscharts.com"
        },
        "JTL Shop": {
            "cats": [
                6
            ],
            "headers": {
                "Set-Cookie": "JTLSHOP="
            },
            "html": "(?:<input[^>]+name=\"JTLSHOP|<a href=\"jtl\\.php)",
            "icon": "JTL Shop.png",
            "website": "www.jtl-software.de/produkte/jtl-shop3"
        },
        "Jalios": {
            "cats": [
                1
            ],
            "icon": "Jalios.png",
            "meta": {
                "generator": "Jalios"
            },
            "website": "www.jalios.com"
        },
        "Java": {
            "cats": [
                27
            ],
            "headers": {
                "Set-Cookie": "JSESSIONID"
            },
            "icon": "Java.png",
            "website": "java.com"
        },
        "Java Servlet": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "Servlet(?:.([\\d.]+))?\\;version:\\1"
            },
            "icon": "Java.png",
            "implies": "Java",
            "website": "www.oracle.com/technetwork/java/index-jsp-135475.html"
        },
        "JavaServer Faces": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "JSF(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "JavaServer Faces.png",
            "implies": "Java",
            "website": "javaserverfaces.java.net"
        },
        "JavaServer Pages": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "JSP(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Java.png",
            "implies": "Java",
            "website": "www.oracle.com/technetwork/java/javaee/jsp/index.html"
        },
        "Javascript Infovis Toolkit": {
            "cats": [
                25
            ],
            "env": "^\\$jit$",
            "icon": "Javascript Infovis Toolkit.png",
            "script": "jit.*\\.js",
            "website": "thejit.org"
        },
        "Jekyll": {
            "cats": [
                1,
                11
            ],
            "icon": "Jekyll.png",
            "meta": {
                "generator": "Jekyll (v[\\d.]+)?\\;version:\\1"
            },
            "website": "jekyllrb.com"
        },
        "Jenkins": {
            "cats": [
                44
            ],
            "headers": {
                "X-Jenkins": "([\\d\\.]+)\\;version:\\1"
            },
            "icon": "Jenkins.png",
            "website": "jenkins-ci.org"
        },
        "Jetty": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Jetty(?:\\(([\\d\\.]*\\d+))?\\;version:\\1"
            },
            "icon": "Jetty.png",
            "implies": "Java",
            "website": "www.eclipse.org/jetty"
        },
        "Jirafe": {
            "cats": [
                10,
                32
            ],
            "env": "^jirafe$",
            "icon": "Jirafe.png",
            "script": "/jirafe\\.js",
            "website": "jirafe.com"
        },
        "Jo": {
            "cats": [
                26,
                12
            ],
            "env": "^jo(?:Cache|DOM|Event)$",
            "icon": "Jo.png",
            "website": "joapp.com"
        },
        "JobberBase": {
            "cats": [
                19
            ],
            "env": "^Jobber$",
            "icon": "JobberBase.png",
            "meta": {
                "generator": "Jobberbase"
            },
            "website": "jobberbase.com"
        },
        "Joomla": {
            "cats": [
                1
            ],
            "env": "^(?:jcomments|Joomla)$",
            "headers": {
                "X-Content-Encoded-By": "Joomla! ([\\d.]+)\\;version:\\1"
            },
            "html": "(?:<div[^>]+id=\"wrapper_r\"|<[^>]+(?:feed|components)/com_|<table[^>]+class=\"pill)",
            "icon": "Joomla.png",
            "implies": "PHP",
            "meta": {
                "generator": "Joomla!(?: ([\\d.]+))?\\;version:\\1"
            },
            "url": "option=com_",
            "website": "joomla.org"
        },
        "K2": {
            "cats": [
                19
            ],
            "env": "^K2RatingURL$",
            "html": "<!--(?: JoomlaWorks \"K2\"| Start K2)",
            "icon": "K2.png",
            "implies": "Joomla",
            "website": "getk2.org"
        },
        "KISSmetrics": {
            "cats": [
                10
            ],
            "env": "^KM_COOKIE_DOMAIN$",
            "icon": "KISSmetrics.png",
            "website": "www.kissmetrics.com"
        },
        "KS_HTTP": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "KS_HTTP\\/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "KS_HTTP.png",
            "implies": "Canon",
            "website": "www.canon.com"
        },
        "Kampyle": {
            "cats": [
                10,
                13
            ],
            "env": "^k_track$",
            "headers": {
                "Set-Cookie": "k_visit"
            },
            "icon": "Kampyle.png",
            "script": "cf\\.kampyle\\.com/k_button\\.js",
            "website": "www.kampyle.com"
        },
        "Kendo UI": {
            "cats": [
                18
            ],
            "env": "^kendo$",
            "html": "<link[^>]*\\s+href=[^>]*styles/kendo\\.common(?:\\.min)?\\.css[^>]*/>",
            "icon": "Kendo UI.png",
            "implies": "jQuery",
            "website": "www.kendoui.com"
        },
        "Kentico CMS": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "CMSPreferredCulture="
            },
            "icon": "Kentico CMS.png",
            "meta": {
                "generator": "Kentico CMS ([\\d.R]+ \\(build [\\d.]+\\))\\;version:\\1"
            },
            "website": "www.kentico.com"
        },
        "KineticJS": {
            "cats": [
                25
            ],
            "env": "^Kinetic$",
            "icon": "KineticJS.png",
            "script": "kinetic(?:-v?([\\d.]+))?(?:\\.min)?\\.js\\;version:\\1",
            "website": "kineticjs.com"
        },
        "Knockout.js": {
            "cats": [
                12
            ],
            "env": "^ko$",
            "icon": "Knockout.js.png",
            "website": "knockoutjs.com"
        },
        "Koa": {
            "cats": [
                18,
                22
            ],
            "headers": {
                "X-Powered-By": "^koa$"
            },
            "icon": "Koa.png",
            "implies": "Node.js",
            "website": "koajs.com"
        },
        "Koala Framework": {
            "cats": [
                1,
                18
            ],
            "html": "<!--[^>]+This website is powered by Koala Web Framework CMS",
            "icon": "Koala Framework.png",
            "implies": "PHP",
            "meta": {
                "generator": "^Koala Web Framework CMS"
            },
            "website": "koala-framework.org"
        },
        "Koego": {
            "cats": [
                10
            ],
            "env": "^ego_domains$",
            "icon": "Koego.png",
            "script": "tracking\\.koego\\.com/end/ego\\.js",
            "website": "www.koego.com/en"
        },
        "Kohana": {
            "cats": [
                18
            ],
            "headers": {
                "Set-Cookie": "kohanasession",
                "X-Powered-By": "Kohana Framework ([\\d.]+)\\;version:\\1"
            },
            "icon": "Kohana.png",
            "implies": "PHP",
            "website": "kohanaframework.org"
        },
        "Koken": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "koken_referrer="
            },
            "html": [
                "<html lang=\"en\" class=\"k-source-essays k-lens-essays\">",
                "<!--\\s+KOKEN DEBUGGING"
            ],
            "icon": "Koken.png",
            "implies": [
                "PHP",
                "MySQL"
            ],
            "meta": {
                "generator": "Koken ([\\d.]+)\\;version:\\1"
            },
            "script": "koken(?:\\.js\\?([\\d.]+)|/storage)\\;version:\\1",
            "website": "koken.me"
        },
        "Kolibri CMS": {
            "cats": [
                1
            ],
            "headers": {
                "X-Powered-By": "Kolibri"
            },
            "icon": "default.png",
            "meta": {
                "generator": "Kolibri"
            },
            "website": "alias.io"
        },
        "Komodo CMS": {
            "cats": [
                1
            ],
            "icon": "Komodo CMS.png",
            "implies": "PHP",
            "meta": {
                "generator": "^Komodo CMS"
            },
            "website": "www.komodocms.com"
        },
        "Koobi": {
            "cats": [
                1
            ],
            "html": "<!--[^K>-]+Koobi ([a-z\\d.]+)\\;version:\\1",
            "icon": "Koobi.png",
            "meta": {
                "generator": "Koobi"
            },
            "website": "dream4.de/cms"
        },
        "Kooboo CMS": {
            "cats": [
                1
            ],
            "headers": {
                "X-KoobooCMS-Version": "(.*)\\;version:\\1"
            },
            "icon": "Kooboo CMS.png",
            "implies": "Microsoft ASP.NET",
            "script": "/Kooboo",
            "website": "kooboo.com"
        },
        "Kotisivukone": {
            "cats": [
                1
            ],
            "icon": "Kotisivukone.png",
            "script": "kotisivukone(?:\\.min)?\\.js",
            "website": "www.kotisivukone.fi"
        },
        "LEPTON": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "lep\\d+sessionid="
            },
            "icon": "LEPTON.png",
            "implies": "PHP",
            "meta": {
                "generator": "LEPTON"
            },
            "website": "www.lepton-cms.org"
        },
        "LabVIEW": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "LabVIEW(?:/([\\d\\.]+))?\\;version:\\1"
            },
            "icon": "LabVIEW.png",
            "website": "ni.com/labview"
        },
        "Laravel": {
            "cats": [
                18
            ],
            "headers": {
                "Set-Cookie": "laravel_session"
            },
            "icon": "Laravel.png",
            "implies": "PHP",
            "website": "laravel.com"
        },
        "Lazy.js": {
            "cats": [
                12
            ],
            "icon": "default.png",
            "script": "lazy(?:\\.browser)?(?:\\.min)?\\.js",
            "website": "danieltao.com/lazy.js"
        },
        "Leaflet": {
            "cats": [
                35
            ],
            "icon": "Leaflet.png",
            "script": "leaflet.*\\.js",
            "website": "leafletjs.com"
        },
        "Less": {
            "cats": [
                19
            ],
            "html": "<link[^>]+ rel=\"stylesheet/less\"",
            "icon": "Less.png",
            "website": "lesscss.org"
        },
        "Liferay": {
            "cats": [
                1
            ],
            "env": "^Liferay$",
            "headers": {
                "Liferay-Portal": "[a-z\\s]+([\\d.]+)\\;version:\\1"
            },
            "icon": "Liferay.png",
            "website": "www.liferay.com"
        },
        "Lift": {
            "cats": [
                18
            ],
            "headers": {
                "X-Lift-Version": "(.+)\\;version:\\1"
            },
            "icon": "Lift.png",
            "implies": "Scala",
            "website": "liftweb.net"
        },
        "LightMon Engine": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "lm_online"
            },
            "html": "<!-- Lightmon Engine Copyright Lightmon",
            "icon": "LightMon Engine.png",
            "implies": [
                "PHP"
            ],
            "meta": {
                "generator": "LightMon Engine"
            },
            "website": "lightmon.ru"
        },
        "Lightbox": {
            "cats": [
                7,
                12
            ],
            "html": "<link [^>]*href=\"[^\"]+lightbox(?:\\.min)?\\.css",
            "icon": "Lightbox.png",
            "script": "lightbox.*\\.js",
            "website": "lokeshdhakar.com/projects/lightbox2/"
        },
        "Lightspeed eCom": {
            "cats": [
                6
            ],
            "html": "<!-- \\[START\\] 'blocks/head.rain' -->",
            "icon": "Lightspeed.svg",
            "script": "http://assets.webshopapp.com",
            "url": "seoshop.webshopapp.com",
            "website": "www.lightspeedhq.com/products/ecommerce/"
        },
        "Lighty": {
            "cats": [
                18
            ],
            "headers": {
                "Set-Cookie": "lighty_version"
            },
            "icon": "Lighty.png",
            "implies": "PHP",
            "website": "gitlab.com/lighty/framework"
        },
        "LimeSurvey": {
            "cats": [
                19
            ],
            "headers": {
                "generator": "LimeSurvey"
            },
            "icon": "LimeSurvey.png",
            "website": "limesurvey.org/"
        },
        "LinkSmart": {
            "cats": [
                36
            ],
            "env": "^(?:_mb_site_guid$|LS_JSON|LinkSmart(?:_|$))",
            "icon": "LinkSmart.png",
            "script": "^https?://cdn\\.linksmart\\.com/linksmart_([\\d.]+?)(?:\\.min)?\\.js\\;version:\\1",
            "website": "linksmart.com"
        },
        "List.js": {
            "cats": [
                12
            ],
            "env": "^List$",
            "icon": "List.js.png",
            "script": "^list\\.(?:min\\.)?js$",
            "website": "www.listjs.com"
        },
        "LiteSpeed": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "^LiteSpeed$"
            },
            "icon": "LiteSpeed.png",
            "website": "litespeedtech.com"
        },
        "Lithium": {
            "cats": [
                1
            ],
            "env": [
                "^LITHIUM$"
            ],
            "headers": {
                "Set-Cookie": "LithiumVisitor="
            },
            "html": " <a [^>]+Powered by Lithium",
            "icon": "Lithium.png",
            "implies": "PHP",
            "website": "www.lithium.com"
        },
        "LiveJournal": {
            "cats": [
                11
            ],
            "icon": "LiveJournal.png",
            "url": "\\.livejournal\\.com",
            "website": "www.livejournal.com"
        },
        "LiveStreet CMS": {
            "cats": [
                1
            ],
            "env": "^LIVESTREET",
            "headers": {
                "X-Powered-By": "LiveStreet CMS"
            },
            "icon": "LiveStreet CMS.png",
            "website": "livestreetcms.com"
        },
        "Livefyre": {
            "cats": [
                15
            ],
            "env": [
                "^fyre$",
                "^FyreLoader$"
            ],
            "html": "<[^>]+(?:id|class)=\"livefyre",
            "icon": "Livefyre.png",
            "script": "livefyre_init\\.js",
            "website": "livefyre.com"
        },
        "Liveinternet": {
            "cats": [
                10
            ],
            "html": [
                "<script[^<>]*>[^]{0,128}?src\\s*=\\s*['\"]//counter\\.yadro\\.ru/hit(?:;\\S+)?\\?(?:t\\d+\\.\\d+;)?r",
                "<!--LiveInternet counter-->",
                "<!--/LiveInternet-->",
                "<a href=\"http://www.liveinternet.ru/click\""
            ],
            "icon": "Liveinternet.png",
            "script": "/js/al/common.js\\?[0-9_]+",
            "website": "liveinternet.ru/rating/"
        },
        "Lo-dash": {
            "cats": [
                12
            ],
            "icon": "Lo-dash.png",
            "script": "lodash.*\\.js",
            "website": "www.lodash.com"
        },
        "Locomotive": {
            "cats": [
                1
            ],
            "html": "<link[^>]*/sites/[a-z\\d]{24}/theme/stylesheets",
            "icon": "Locomotive.png",
            "implies": [
                "Ruby on Rails",
                "MongoDB"
            ],
            "website": "www.locomotivecms.com"
        },
        "Logitech Media Server": {
            "cats": [
                22,
                38
            ],
            "headers": {
                "Server": "Logitech Media Server(?: \\(([\\d\\.]+))?\\;version:\\1"
            },
            "icon": "Logitech Media Server.png",
            "website": "www.mysqueezebox.com"
        },
        "Lotus Domino": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Lotus-Domino"
            },
            "icon": "Lotus Domino.png",
            "website": "www-01.ibm.com/software/lotus/products/domino"
        },
        "Lua": {
            "cats": [
                27
            ],
            "headers": {
                "X-Powered-By": "\bLua(?: ([\\d.]+))?\\;version:\\1"
            },
            "icon": "Lua.png",
            "website": "www.lua.org"
        },
        "Lucene": {
            "cats": [
                34
            ],
            "icon": "Lucene.png",
            "website": "lucene.apache.org/core/"
        },
        "M.R. Inc BoxyOS": {
            "cats": [
                28
            ],
            "icon": "M.R. Inc BoxyOS.png",
            "website": "mrincworld.com"
        },
        "M.R. Inc SiteFrame": {
            "cats": [
                18
            ],
            "headers": {
                "Powered-By": "M\\.R\\. Inc SiteFrame"
            },
            "icon": "M.R. Inc SiteFrame.png",
            "website": "mrincworld.com"
        },
        "M.R. Inc Webserver": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "M\\.R\\. Inc Webserver"
            },
            "icon": "M.R. Inc Webserver.png",
            "implies": [
                "M.R. Inc BoxyOS"
            ],
            "website": "mrincworld.com"
        },
        "MOBOTIX": {
            "cats": [
                39
            ],
            "icon": "MOBOTIX.png",
            "meta": {
                "author": "MOBOTIX AG",
                "copyright": "MOBOTIX AG",
                "publisher": "MOBOTIX AG"
            },
            "url": "control/userimage\\.html",
            "website": "mobotix.com"
        },
        "MODx": {
            "cats": [
                1
            ],
            "env": "^MODX_MEDIA_PATH$",
            "headers": {
                "Set-Cookie": "SN4[a-f\\d]{12}",
                "X-Powered-By": "^MODx"
            },
            "html": [
                "<a[^>]+>Powered by MODx</a>",
                "<(?:link|script)[^>]+assets/snippets/"
            ],
            "icon": "MODx.png",
            "implies": "PHP",
            "website": "modxcms.com"
        },
        "MadAdsMedia": {
            "cats": [
                36
            ],
            "env": "^setM(?:Iframe|RefURL)$",
            "icon": "MadAdsMedia.png",
            "script": "^https?://(?:ads-by|pixel)\\.madadsmedia.com/",
            "website": "madadsmedia.com"
        },
        "Magento": {
            "cats": [
                6
            ],
            "env": [
                "^(?:Mage|VarienForm)$"
            ],
            "headers": {
                "Set-Cookie": "frontend="
            },
            "html": [
                "<script [^>]+data-requiremodule=\"mage/\\;version:2",
                "<script [^>]+data-requiremodule=\"Magento_\\;version:2"
            ],
            "icon": "Magento.png",
            "implies": "PHP",
            "script": [
                "js/mage",
                "skin/frontend/(?:default|(enterprise))\\;version:\\1?Enterprise:Community",
                "static/_requirejs\\;version:2",
                "static/frontend\\;version:2"
            ],
            "website": "www.magentocommerce.com"
        },
        "Mambo": {
            "cats": [
                1
            ],
            "excludes": "Joomla",
            "icon": "Mambo.png",
            "meta": {
                "generator": "Mambo"
            },
            "website": "mambo-foundation.org"
        },
        "MantisBT": {
            "cats": [
                13
            ],
            "html": "<img[^>]+ alt=\"Powered by Mantis Bugtracker",
            "icon": "MantisBT.png",
            "website": "www.mantisbt.org"
        },
        "ManyContacts": {
            "cats": [
                5
            ],
            "icon": "ManyContacts.png",
            "script": "\\/assets\\/js\\/manycontacts\\.min\\.js",
            "website": "www.manycontacts.com"
        },
        "Marionette.js": {
            "cats": [
                12
            ],
            "env": "^Marionette$",
            "icon": "Marionette.js.svg",
            "implies": [
                "Underscore.js",
                "Backbone.js"
            ],
            "script": "backbone\\.marionette.*\\.js",
            "website": "marionettejs.com"
        },
        "Marketo": {
            "cats": [
                32
            ],
            "env": "^Munchkin$",
            "icon": "Marketo.png",
            "script": "munchkin\\.marketo\\.net/munchkin\\.js",
            "website": "www.marketo.com"
        },
        "Materialize CSS": {
            "cats": [
                18
            ],
            "html": "<link[^>]* href=\"[^\"]*materialize(?:\\.min)?\\.css",
            "icon": "Materialize CSS.png",
            "implies": "jQuery",
            "script": "materialize(?:\\.min)?\\.js",
            "website": "materializecss.com"
        },
        "MathJax": {
            "cats": [
                25
            ],
            "env": "^MathJax$",
            "icon": "MathJax.png",
            "script": "mathjax\\.js",
            "website": "mathjax.org"
        },
        "MaxCDN": {
            "cats": [
                31
            ],
            "headers": {
                "Server": "NetDNA"
            },
            "icon": "MaxCDN.png",
            "website": "www.maxcdn.com"
        },
        "MaxSite CMS": {
            "cats": [
                1
            ],
            "icon": "MaxSite CMS.png",
            "meta": {
                "generator": "MaxSite CMS"
            },
            "website": "max-3000.com"
        },
        "Mean.io": {
            "cats": [
                12
            ],
            "headers": {
                "X-Powered-CMS": "Mean\\.io"
            },
            "icon": "Mean.io.png",
            "implies": [
                "MongoDB",
                "Express",
                "AngularJS",
                "Node.js"
            ],
            "website": "mean.io"
        },
        "MediaElement.js": {
            "cats": [
                14
            ],
            "env": "^mejs$",
            "icon": "MediaElement.js.png",
            "website": "mediaelementjs.com"
        },
        "MediaTomb": {
            "cats": [
                38
            ],
            "headers": {
                "Server": "MediaTomb(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "MediaTomb.png",
            "website": "mediatomb.cc"
        },
        "MediaWiki": {
            "cats": [
                8
            ],
            "html": "(?:<a[^>]+>Powered by MediaWiki</a>|<[^>]+id=\"t-specialpages)",
            "icon": "MediaWiki.png",
            "meta": {
                "generator": "MediaWiki"
            },
            "website": "www.mediawiki.org"
        },
        "Meebo": {
            "cats": [
                5
            ],
            "html": "(?:<iframe id=\"meebo-iframe\"|Meebo\\('domReady'\\))",
            "icon": "Meebo.png",
            "website": "www.meebo.com"
        },
        "Meteor": {
            "cats": [
                12
            ],
            "env": "^Meteor$",
            "html": "<link[^>]+__meteor-css__",
            "icon": "Meteor.png",
            "website": "meteor.com"
        },
        "Methode": {
            "cats": [
                1
            ],
            "env": "^eidosBase$",
            "html": "<!-- Methode uuid: \"[a-f\\d]+\" ?-->",
            "icon": "Methode.png",
            "meta": {
                "eomportal-id": "\\d+",
                "eomportal-instanceid": "\\d+",
                "eomportal-lastUpdate": "",
                "eomportal-loid": "[\\d.]+",
                "eomportal-uuid": "[a-f\\d]+"
            },
            "website": "www.eidosmedia.com/solutions"
        },
        "Microsoft ASP.NET": {
            "cats": [
                18
            ],
            "headers": {
                "Set-Cookie": "ASPSESSION|ASP\\.NET_SessionId",
                "X-AspNet-Version": "(.+)\\;version:\\1",
                "X-Powered-By": "ASP\\.NET"
            },
            "html": "<input[^>]+name=\"__VIEWSTATE",
            "icon": "Microsoft ASP.NET.png",
            "implies": "IIS",
            "url": "\\.aspx(?:$|\\?)",
            "website": "www.asp.net"
        },
        "Microsoft HTTPAPI": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Microsoft-HTTPAPI(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Microsoft.svg",
            "website": "microsoft.com"
        },
        "Microsoft SharePoint": {
            "cats": [
                1
            ],
            "env": "^_spBodyOnLoadCalled$",
            "headers": {
                "MicrosoftSharePointTeamServices": "(.*)\\;version:\\1",
                "SPRequestGuid": "",
                "SharePointHealthScore": "",
                "X-SharePointHealthScore": ""
            },
            "icon": "Microsoft SharePoint.png",
            "meta": {
                "generator": "Microsoft SharePoint"
            },
            "website": "sharepoint.microsoft.com"
        },
        "Mietshop": {
            "cats": [
                6
            ],
            "html": "<a href=\"https://ssl.mietshop.d",
            "icon": "mietshop.png",
            "meta": {
                "generator": "Mietshop"
            },
            "website": "www.mietshop.de/"
        },
        "Milligram": {
            "cats": [
                18
            ],
            "html": [
                "<link[^>]+?href=\"[^\"]+milligram(?:\\.min)?\\.css"
            ],
            "icon": "Milligram.png",
            "website": "milligram.github.io"
        },
        "MiniBB": {
            "cats": [
                2
            ],
            "html": "<a href=\"[^\"]+minibb[^<]+</a>[^<]+\n<!--End of copyright link",
            "icon": "MiniBB.png",
            "website": "www.minibb.com"
        },
        "MiniServ": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "MiniServ\\/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "sourceforge.net/projects/miniserv"
        },
        "Mint": {
            "cats": [
                10
            ],
            "env": "^Mint$",
            "icon": "Mint.png",
            "script": "mint/\\?js",
            "website": "haveamint.com"
        },
        "Mixpanel": {
            "cats": [
                10
            ],
            "env": "^Mixpanel$",
            "icon": "Mixpanel.png",
            "script": "api\\.mixpanel\\.com/track",
            "website": "mixpanel.com"
        },
        "Mobify": {
            "cats": [
                26
            ],
            "env": "^Mobify$",
            "icon": "Mobify.png",
            "script": "mobify\\.com",
            "website": "www.mobify.com"
        },
        "MochiKit": {
            "cats": [
                12
            ],
            "env": "^MochiKit$",
            "icon": "MochiKit.png",
            "script": "MochiKit(?:\\.min)?\\.js",
            "website": "mochikit.com"
        },
        "MochiWeb": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "MochiWeb(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "github.com/mochi/mochiweb"
        },
        "Modernizr": {
            "cats": [
                12
            ],
            "env": "^Modernizr$",
            "icon": "Modernizr.png",
            "script": "modernizr(?:-([\\d.]*[\\d]))?.*\\.js\\;version:\\1",
            "website": "www.modernizr.com"
        },
        "Modified": {
            "cats": [
                6
            ],
            "icon": "modified.png",
            "meta": {
                "generator": "\\(c\\) by modified eCommerce Shopsoftware ------ http://www.modified-shop.org"
            },
            "website": "www.modified-shop.org/"
        },
        "Moguta.CMS": {
            "cats": [
                1,
                6
            ],
            "html": "(?:<script|link)[^>]*mg-(?:core|plugins|templates)",
            "icon": "Moguta.CMS.png",
            "implies": "PHP",
            "website": "moguta.ru"
        },
        "MoinMoin": {
            "cats": [
                8
            ],
            "env": "^show_switch2gui$",
            "icon": "MoinMoin.png",
            "implies": "Python",
            "script": "moin(?:_static(\\d)(\\d)(\\d)|.+)/common/js/common\\.js\\;version:\\1.\\2.\\3",
            "website": "moinmo.in"
        },
        "Mojolicious": {
            "cats": [
                18
            ],
            "headers": {
                "x-powered-by": "mojolicious"
            },
            "icon": "Mojolicious.png",
            "implies": "Perl",
            "website": "mojolicio.us"
        },
        "Mollom": {
            "cats": [
                16
            ],
            "html": "<img[^>]+\\.mollom\\.com",
            "icon": "Mollom.png",
            "script": "mollom(?:\\.min)?\\.js",
            "website": "mollom.com"
        },
        "Moment Timezone": {
            "cats": [
                12
            ],
            "icon": "Moment Timezone.png",
            "implies": "Moment.js",
            "script": "moment-timezone(?:\\-data)?(?:\\.min)?\\.js",
            "website": "momentjs.com/timezone/"
        },
        "Moment.js": {
            "cats": [
                12
            ],
            "env": "^moment$",
            "icon": "Moment.js.png",
            "script": "moment(?:\\.min)?\\.js",
            "website": "momentjs.com"
        },
        "Mondo Media": {
            "cats": [
                6
            ],
            "icon": "Mondo Media.png",
            "meta": {
                "generator": "Mondo Shop"
            },
            "website": "mondo-media.de"
        },
        "MongoDB": {
            "cats": [
                34
            ],
            "icon": "MongoDB.png",
            "website": "www.mongodb.org"
        },
        "Mongrel": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Mongrel"
            },
            "icon": "Mongrel.png",
            "implies": "Ruby",
            "website": "mongrel2.org"
        },
        "Monkey HTTP Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Monkey/?([\\d.]+)?\\;version:\\1"
            },
            "icon": "Monkey HTTP Server.png",
            "website": "monkey-project.com"
        },
        "Mono": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "Mono"
            },
            "icon": "Mono.png",
            "website": "mono-project.com"
        },
        "Mono.net": {
            "cats": [
                1
            ],
            "env": "^_monoTracker$",
            "icon": "Mono.net.png",
            "implies": "Piwik",
            "script": "monotracker(?:\\.min)?\\.js",
            "website": "www.mono.net"
        },
        "MooTools": {
            "cats": [
                12
            ],
            "env": "^MooTools$",
            "icon": "MooTools.png",
            "script": "mootools.*\\.js",
            "website": "mootools.net"
        },
        "Moodle": {
            "cats": [
                21
            ],
            "env": "^moodle",
            "headers": {
                "Set-Cookie": "MoodleSession"
            },
            "html": "<img[^>]+moodlelogo",
            "icon": "Moodle.png",
            "implies": "PHP",
            "website": "moodle.org"
        },
        "Motion-httpd": {
            "cats": [
                22
            ],
            "excludes": "Apache",
            "headers": {
                "Server": "Motion-httpd(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "lavrsen.dk/foswiki/bin/view/Motion"
        },
        "MotoCMS": {
            "cats": [
                1
            ],
            "html": "<link [^>]*href=\"[^>]*\\/mt-content\\/[^>]*\\.css",
            "icon": "MotoCMS.svg",
            "implies": [
                "PHP",
                "AngularJS",
                "jQuery"
            ],
            "script": ".*\\/mt-includes\\/[asetj]{2,6}\\/.*\\.js.*",
            "website": "motocms.com"
        },
        "Movable Type": {
            "cats": [
                1
            ],
            "icon": "Movable Type.png",
            "meta": {
                "generator": "Movable Type"
            },
            "website": "movabletype.org"
        },
        "Moxa": {
            "cats": [
                37
            ],
            "headers": {
                "Server": "MoxaHttp(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Moxa.png",
            "website": "moxa.com"
        },
        "Mozard Suite": {
            "cats": [
                1
            ],
            "icon": "Mozard Suite.png",
            "meta": {
                "author": "Mozard"
            },
            "url": "/mozard/!suite",
            "website": "mozard.nl"
        },
        "Mura CMS": {
            "cats": [
                1,
                11
            ],
            "icon": "Mura CMS.png",
            "implies": "Adobe ColdFusion",
            "meta": {
                "generator": "Mura CMS ([\\d]+)\\;version:\\1"
            },
            "website": "www.getmura.com"
        },
        "Mustache": {
            "cats": [
                12
            ],
            "env": "^Mustache$",
            "icon": "Mustache.png",
            "script": "mustache(?:\\.min)?\\.js",
            "website": "mustache.github.com"
        },
        "MyBB": {
            "cats": [
                2
            ],
            "env": "^MyBB$",
            "html": "(?:<script [^>]+\\s+<!--\\s+lang\\.no_new_posts|<a[^>]* title=\"Powered By MyBB)",
            "icon": "MyBB.png",
            "implies": [
                "PHP",
                "MySQL"
            ],
            "website": "www.mybb.com"
        },
        "MyBlogLog": {
            "cats": [
                5
            ],
            "icon": "MyBlogLog.png",
            "script": "pub\\.mybloglog\\.com",
            "website": "www.mybloglog.com"
        },
        "MySQL": {
            "cats": [
                34
            ],
            "icon": "MySQL.svg",
            "website": "mysql.com"
        },
        "Mynetcap": {
            "cats": [
                1
            ],
            "icon": "Mynetcap.png",
            "meta": {
                "generator": "Mynetcap"
            },
            "website": "www.netcap-creation.fr"
        },
        "NOIX": {
            "cats": [
                19
            ],
            "html": "(?:<[^>]+(?:src|href)=[^>]*/media/noix|<!-- NOIX)",
            "icon": "NOIX.png",
            "website": "www.noix.com.br/tecnologias/joomla"
        },
        "NVD3": {
            "cats": [
                25
            ],
            "env": "^nv$",
            "html": "<link[^>]* href=[^>]+nv\\.d3(?:\\.min)?\\.css",
            "icon": "NVD3.png",
            "implies": "D3",
            "script": "nv\\.d3(?:\\.min)?\\.js",
            "website": "nvd3.org"
        },
        "Nedstat": {
            "cats": [
                10
            ],
            "env": "^sitestat$",
            "icon": "Nedstat.png",
            "website": "www.nedstat.com"
        },
        "Nepso": {
            "cats": [
                1
            ],
            "headers": {
                "X-Powered-CMS": "Nepso"
            },
            "icon": "Nepso.png",
            "implies": [
                "Python",
                "Perl",
                "Java",
                "PHP"
            ],
            "website": "nepso.com"
        },
        "Netmonitor": {
            "cats": [
                10
            ],
            "env": "^netmonitor$",
            "icon": "Netmonitor.png",
            "script": "netmonitor\\.fi/nmtracker\\.js",
            "website": "netmonitor.fi/en"
        },
        "Netsuite": {
            "cats": [
                6
            ],
            "headers": {
                "Set-Cookie": "NS_VER="
            },
            "icon": "Netsuite.png",
            "website": "netsuite.com"
        },
        "Nette Framework": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "Nette Framework"
            },
            "icon": "Nette Framework.png",
            "implies": "PHP",
            "website": "nette.org"
        },
        "New Relic": {
            "cats": [
                10
            ],
            "env": "^NREUM",
            "icon": "New Relic.png",
            "website": "newrelic.com"
        },
        "Nginx": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "nginx(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Nginx.svg",
            "website": "nginx.org"
        },
        "Node.js": {
            "cats": [
                27
            ],
            "icon": "node.js.png",
            "website": "nodejs.org"
        },
        "OWL Carousel": {
            "cats": [
                5,
                7
            ],
            "html": "<link [^>]*href=\"[^\"]+owl.carousel(?:\\.min)?\\.css",
            "icon": "OWL Carousel.png",
            "implies": "jQuery",
            "script": "owl.carousel.*\\.js",
            "website": "owlgraphic.com/owlcarousel"
        },
        "OXID eShop": {
            "cats": [
                6
            ],
            "env": "^ox(?:TopMenu|ModalPopup|LoginBox|InputValidator)",
            "html": "<!--[^-]*OXID eShop",
            "icon": "OXID eShop.png",
            "website": "oxid-esales.com"
        },
        "October CMS": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "october_session="
            },
            "icon": "October CMS.png",
            "implies": "Laravel",
            "website": "octobercms.com"
        },
        "Odoo": {
            "cats": [
                1,
                6
            ],
            "html": "<link[^>]* href=[^>]+/web/css/(?:web\\.assets_common/|website\\.assets_frontend/)",
            "icon": "Odoo.png",
            "implies": [
                "Python",
                "PostgreSQL",
                "Node.js",
                "Less"
            ],
            "meta": {
                "generator": "Odoo"
            },
            "script": "/web/js/(?:web\\.assets_common/|website\\.assets_frontend/)",
            "website": "odoo.com"
        },
        "OmniTouch 8660 My Teamwork": {
            "cats": [
                19
            ],
            "icon": "OmniTouch 8660 My Teamwork.png",
            "website": "enterprise.alcatel-lucent.com"
        },
        "OneAPM": {
            "cats": [
                10
            ],
            "env": "^BWEUM",
            "icon": "OneAPM.png",
            "website": "www.oneapm.com"
        },
        "OneStat": {
            "cats": [
                10
            ],
            "env": "^OneStat",
            "icon": "OneStat.png",
            "website": "www.onestat.com"
        },
        "Open AdStream": {
            "cats": [
                36
            ],
            "env": "^OAS_AD$",
            "icon": "Open AdStream.png",
            "website": "xaxis.com"
        },
        "Open Classifieds": {
            "cats": [
                6
            ],
            "icon": "Open Classifieds.png",
            "meta": {
                "author": "open-classifieds\\.com",
                "copyright": "Open Classifieds ?([0-9.]+)?\\;version:\\1"
            },
            "website": "open-classifieds.com"
        },
        "Open Journal Systems": {
            "cats": [
                50
            ],
            "headers": {
                "Set-Cookie": "\bOJSSID\b"
            },
            "icon": "Open Journal Systems.png",
            "implies": [
                "PHP"
            ],
            "meta": {
                "generator": "Open Journal Systems(?: ([\\d.]+))?\\;version:\\1"
            },
            "website": "pkp.sfu.ca/ojs"
        },
        "Open Web Analytics": {
            "cats": [
                10
            ],
            "env": "^_?owa_",
            "html": "<!-- (?:Start|End) Open Web Analytics Tracker -->",
            "icon": "Open Web Analytics.png",
            "website": "openwebanalytics.com"
        },
        "Open eShop": {
            "cats": [
                6
            ],
            "icon": "Open eShop.png",
            "meta": {
                "author": "open-eshop\\.com",
                "copyright": "Open eShop ?([0-9.]+)?\\;version:\\1"
            },
            "website": "open-eshop.com/"
        },
        "OpenCart": {
            "cats": [
                6
            ],
            "html": "(?:index\\.php\\?route=[a-z]+/|Powered By <a href=\"[^>]+OpenCart)",
            "icon": "OpenCart.png",
            "implies": "PHP",
            "website": "www.opencart.com"
        },
        "OpenCms": {
            "cats": [
                1
            ],
            "headers": {
                "Server": "OpenCms"
            },
            "html": "<link href=\"/opencms/",
            "icon": "OpenCms.png",
            "implies": "Java",
            "script": "opencms",
            "website": "www.opencms.org"
        },
        "OpenGSE": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "GSE"
            },
            "icon": "OpenGSE.png",
            "implies": "Java",
            "website": "code.google.com/p/opengse"
        },
        "OpenGrok": {
            "cats": [
                19
            ],
            "headers": {
                "Set-Cookie": "OpenGrok"
            },
            "icon": "OpenGrok.png",
            "implies": "Java",
            "meta": {
                "generator": "OpenGrok(?: v?([\\d.]+))?\\;version:\\1"
            },
            "website": "hub.opensolaris.org/bin/view/Project+opengrok/WebHome"
        },
        "OpenLayers": {
            "cats": [
                35
            ],
            "env": "^OpenLayers$",
            "icon": "OpenLayers.png",
            "script": "openlayers",
            "website": "openlayers.org"
        },
        "OpenNemas": {
            "cats": [
                1
            ],
            "headers": {
                "X-Powered-By": "OpenNemas"
            },
            "icon": "OpenNemas.png",
            "meta": {
                "generator": "OpenNemas"
            },
            "website": "www.opennemas.com"
        },
        "OpenResty": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "openresty(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "OpenResty.png",
            "implies": [
                "Nginx",
                "Lua"
            ],
            "website": "openresty.org"
        },
        "OpenSSL": {
            "cats": [
                33
            ],
            "headers": {
                "Server": "OpenSSL(?:/([\\d.]+[a-z]?))?\\;version:\\1"
            },
            "icon": "OpenSSL.png",
            "website": "openssl.org"
        },
        "OpenText Web Solutions": {
            "cats": [
                1
            ],
            "html": "<!--[^>]+published by Open Text Web Solutions",
            "icon": "OpenText Web Solutions.png",
            "implies": "Microsoft ASP.NET",
            "website": "websolutions.opentext.com"
        },
        "OpenX": {
            "cats": [
                36
            ],
            "icon": "OpenX.png",
            "script": [
                "https?://[^/]*\\.openx\\.net",
                "https?://[^/]*\\.servedbyopenx\\.com"
            ],
            "website": "openx.com"
        },
        "Ophal": {
            "cats": [
                1,
                11,
                18
            ],
            "headers": {
                "X-Powered-By": "Ophal(?: (.*))? \\(ophal\\.org\\)\\;version:\\1"
            },
            "icon": "Ophal.png",
            "implies": "Lua",
            "meta": {
                "generator": "Ophal(?: (.*))? \\(ophal\\.org\\)\\;version:\\1"
            },
            "script": "ophal\\.js",
            "website": "ophal.org"
        },
        "Optimizely": {
            "cats": [
                10
            ],
            "env": "^optimizely$",
            "icon": "Optimizely.png",
            "script": "optimizely\\.com.*\\.js",
            "website": "optimizely.com"
        },
        "Oracle Application Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Oracle[- ]Application[- ]Server(?: Containers for J2EE)?(?:[- ](\\d[\\da-z./]+))?\\;version:\\1"
            },
            "icon": "Oracle.png",
            "website": "www.oracle.com/technetwork/middleware/ias/overview/index.html"
        },
        "Oracle Commerce": {
            "cats": [
                6
            ],
            "headers": {
                "X-ATG-Version": "(?:ATGPlatform/([\\d.]+))?\\;version:\\1"
            },
            "html": "<[^>]+_dyncharset",
            "icon": "Oracle.png",
            "website": "www.oracle.com/applications/customer-experience/commerce/products/commerce-platform/index.html"
        },
        "Oracle Commerce Cloud": {
            "cats": [
                6
            ],
            "headers": {
                "OracleCommerceCloud-Version": "(.*)\\;version:\\1"
            },
            "html": "<[^>]+id=\"oracle-cc\"",
            "icon": "Oracle.png",
            "website": "cloud.oracle.com/commerce-cloud"
        },
        "Oracle Dynamic Monitoring Service": {
            "cats": [
                19
            ],
            "headers": {
                "x-oracle-dms-ecid": ""
            },
            "icon": "Oracle.png",
            "website": "oracle.com"
        },
        "Oracle HTTP Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Oracle-HTTP-Server(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Oracle.png",
            "website": "oracle.com"
        },
        "Oracle Recommendations On Demand": {
            "cats": [
                10
            ],
            "icon": "Oracle.png",
            "script": "atgsvcs.+atgsvcs\\.js",
            "website": "www.oracle.com/us/products/applications/commerce/recommendations-on-demand/index.html"
        },
        "Oracle Web Cache": {
            "cats": [
                23
            ],
            "headers": {
                "Server": "Oracle(?:AS)?[- ]Web[- ]Cache(?:[- /]([\\da-z./]+))?\\;version:\\1"
            },
            "icon": "Oracle.png",
            "website": "oracle.com"
        },
        "Orchard CMS": {
            "cats": [
                1
            ],
            "icon": "Orchard CMS.png",
            "implies": "Microsoft ASP.NET",
            "meta": {
                "generator": "Orchard"
            },
            "website": "orchardproject.net"
        },
        "Outbrain": {
            "cats": [
                5
            ],
            "env": "^(?:OutbrainPermaLink|OB_releaseVer)$",
            "icon": "Outbrain.png",
            "script": "widgets\\.outbrain\\.com/outbrain\\.js",
            "website": "outbrain.com"
        },
        "Outlook Web App": {
            "cats": [
                30
            ],
            "env": "^(?:(?:g_f)?Owa|IsOwaPremiumBrowser)$",
            "html": "<link\\s[^>]*href=\"[^\"]*?([\\d.]+)/themes/resources/owafont\\.css\\;version:\\1",
            "icon": "Outlook Web App.png",
            "implies": "Microsoft ASP.NET",
            "url": "/owa/auth/log(?:on|off)\\.aspx",
            "website": "help.outlook.com"
        },
        "PANSITE": {
            "cats": [
                1
            ],
            "icon": "PANSITE.png",
            "meta": {
                "generator": "PANSITE"
            },
            "website": "panvision.de/Produkte/Content_Management/index.asp"
        },
        "PDF.js": {
            "cats": [
                19
            ],
            "env": "^PDFJS$",
            "html": "<\\/div>\\s*<!-- outerContainer -->\\s*<div\\s*id=\"printContainer\"><\\/div>",
            "icon": "PDF.js.svg",
            "url": "/web/viewer\\.html?file=[^&]\\.pdf",
            "website": "mozilla.github.io/pdf.js/"
        },
        "PHP": {
            "cats": [
                27
            ],
            "headers": {
                "Server": "php/?([\\d.]+)?\\;version:\\1",
                "Set-Cookie": "PHPSESSID",
                "X-Powered-By": "php/?([\\d.]+)?\\;version:\\1"
            },
            "icon": "PHP.png",
            "url": "\\.php(?:$|\\?)",
            "website": "php.net"
        },
        "PHP-Fusion": {
            "cats": [
                1
            ],
            "html": "Powered by <a href=\"[^>]+php-fusion",
            "icon": "PHP-Fusion.png",
            "implies": "PHP",
            "website": "www.php-fusion.co.uk"
        },
        "PHP-Nuke": {
            "cats": [
                2
            ],
            "html": "<[^>]+Powered by PHP-Nuke",
            "icon": "PHP-Nuke.png",
            "implies": "PHP",
            "meta": {
                "generator": "PHP-Nuke"
            },
            "website": "phpnuke.org"
        },
        "Pagekit": {
            "cats": [
                1
            ],
            "icon": "Pagekit.png",
            "meta": {
                "generator": "Pagekit"
            },
            "website": "pagekit.com"
        },
        "Pardot": {
            "cats": [
                32
            ],
            "env": "^pi(?:Tracker|Hostname|Protocol|CId|AId)$",
            "icon": "Pardot.png",
            "website": "pardot.com"
        },
        "Parse.ly": {
            "cats": [
                10
            ],
            "env": "^PARSELY$",
            "icon": "Parse.ly.png",
            "website": "parse.ly"
        },
        "Paths.js": {
            "cats": [
                25
            ],
            "icon": "default.png",
            "script": "paths(?:\\.min)?\\.js",
            "website": "github.com/andreaferretti/paths-js"
        },
        "PayPal": {
            "cats": [
                41
            ],
            "env": "^PAYPAL$",
            "html": "<input[^>]+_s-xclick",
            "icon": "PayPal.png",
            "script": "paypalobjects\\.com/js",
            "website": "paypal.com"
        },
        "PencilBlue": {
            "cats": [
                1,
                11
            ],
            "headers": {
                "X-Powered-By": "PencilBlue"
            },
            "icon": "PencilBlue.png",
            "website": "pencilblue.org"
        },
        "Penguin": {
            "cats": [
                18
            ],
            "env": "^penguin$",
            "html": "<link[^>]+?href=\"[^\"]+penguin(?:\\.min)?\\.css",
            "icon": "Penguin.svg",
            "script": "penguin(?:\\.min)?\\.js",
            "website": "penguin.docs.bqws.io"
        },
        "Percussion": {
            "cats": [
                1
            ],
            "html": "<[^>]+class=\"perc-region\"",
            "icon": "Percussion.png",
            "meta": {
                "generator": "(?:Percussion|Rhythmyx)"
            },
            "website": "percussion.com"
        },
        "PerfSONAR-PS": {
            "cats": [
                19
            ],
            "headers": {
                "User-agent": "perfSONAR-PS/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "PerfSONAR-PS.png",
            "website": "psps.perfsonar.net"
        },
        "Perl": {
            "cats": [
                27
            ],
            "headers": {
                "Server": "\bPerl\b(?: ?/?v?([\\d.]+))?\\;version:\\1"
            },
            "icon": "Perl.png",
            "url": "\\.pl(?:$|\\?)",
            "website": "perl.org"
        },
        "Petrojs": {
            "cats": [
                12
            ],
            "env": "^petrojs$",
            "icon": "Petrojs.png",
            "script": [
                "petrojs(?:\\-|\\.)([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
                "(?:/([\\d.]+)/)?petrojs(?:\\.min)?\\.js\\;version:\\1"
            ],
            "website": "petrojs.thepetronics.com"
        },
        "Phaser": {
            "cats": [
                12
            ],
            "env": "Phaser",
            "icon": "Phaser.png",
            "website": "phaser.io"
        },
        "Phusion Passenger": {
            "cats": [
                22
            ],
            "headers": {
                "X-Powered-By": "^Phusion Passenger"
            },
            "icon": "Phusion Passenger.png",
            "website": "phusionpassenger.com"
        },
        "Piano Solo": {
            "cats": [
                43
            ],
            "env": "^PianoMedia$",
            "headers": {
                "Set-Cookie": "pianovisitkey"
            },
            "icon": "Piano Solo.png",
            "website": "www.pianomedia.com/products"
        },
        "Pimcore": {
            "cats": [
                1,
                6,
                18
            ],
            "headers": {
                "X-Powered-By": "pimcore"
            },
            "icon": "pimcore.svg",
            "implies": [
                "PHP"
            ],
            "website": "pimcore.org"
        },
        "Piwik": {
            "cats": [
                10
            ],
            "env": [
                "^Piwik$",
                "^_paq$"
            ],
            "headers": {
                "Set-Cookie": "PIWIK_SESSID="
            },
            "icon": "Piwik.png",
            "meta": {
                "apple-itunes-app": "app-id=737216887",
                "generator": "Piwik - Open Source Web Analytics",
                "google-play-app": "app-id=org\\.piwik\\.mobile2"
            },
            "script": "piwik\\.js|piwik\\.php",
            "website": "piwik.org"
        },
        "Planet": {
            "cats": [
                49
            ],
            "icon": "Planet.png",
            "meta": {
                "generator": "^Planet(?:/([\\d.]+))?\\;version:\\1"
            },
            "website": "planetplanet.org"
        },
        "Plentymarkets": {
            "cats": [
                6
            ],
            "icon": "Plentymarkets.png",
            "meta": {
                "generator": "plentymarkets"
            },
            "website": "plentymarkets.eu"
        },
        "Plesk": {
            "cats": [
                9
            ],
            "headers": {
                "X-Powered-By": "PleskLin",
                "X-Powered-By-Plesk": "Plesk"
            },
            "icon": "Plesk.png",
            "script": "common\\.js\\?plesk",
            "website": "plesk.com"
        },
        "Pligg": {
            "cats": [
                1
            ],
            "env": "^pligg_",
            "html": "<span[^>]+id=\"xvotes-0",
            "icon": "Pligg.png",
            "meta": {
                "generator": "Pligg"
            },
            "website": "pligg.com"
        },
        "Plone": {
            "cats": [
                1
            ],
            "icon": "Plone.png",
            "implies": "Python",
            "meta": {
                "generator": "Plone"
            },
            "website": "plone.org"
        },
        "Plura": {
            "cats": [
                19
            ],
            "html": "<iframe src=\"[^>]+pluraserver\\.com",
            "icon": "Plura.png",
            "website": "www.pluraprocessing.com"
        },
        "Po.st": {
            "cats": [
                5
            ],
            "env": "^pwidget_config$",
            "icon": "Po.st.png",
            "website": "www.po.st/"
        },
        "Polymer": {
            "cats": [
                12
            ],
            "env": "^Polymer$",
            "html": "(?:<polymer-[^>]+|<link[^>]+rel=\"import\"[^>]+/polymer\\.html\")",
            "icon": "Polymer.png",
            "script": "polymer\\.js",
            "website": "polymer-project.org"
        },
        "Posterous": {
            "cats": [
                1,
                11
            ],
            "env": "^Posterous",
            "html": "<div class=\"posterous",
            "icon": "Posterous.png",
            "website": "posterous.com"
        },
        "PostgreSQL": {
            "cats": [
                34
            ],
            "icon": "PostgreSQL.png",
            "website": "www.postgresql.org/"
        },
        "Powergap": {
            "cats": [
                6
            ],
            "html": [
                "<a[^>]+title=\"POWERGAP",
                "<input type=\"hidden\" name=\"shopid\""
            ],
            "icon": "Powergap.png",
            "website": "powergap.de"
        },
        "Prefix-Free": {
            "cats": [
                19
            ],
            "env": "^PrefixFree$",
            "icon": "Prefix-Free.png",
            "script": "prefixfree\\.js",
            "website": "leaverou.github.io/prefixfree/"
        },
        "PrestaShop": {
            "cats": [
                6
            ],
            "env": [
                "^freeProductTranslation$",
                "^freeProductTranslation$",
                "^priceDisplayMethod$",
                "^priceDisplayPrecision$"
            ],
            "html": "Powered by <a\\s+[^>]+>PrestaShop",
            "icon": "PrestaShop.png",
            "implies": "PHP",
            "meta": {
                "generator": "PrestaShop"
            },
            "website": "www.prestashop.com"
        },
        "Project Wonderful": {
            "cats": [
                36
            ],
            "env": "^pw_adloader$",
            "html": "<div[^>]+id=\"pw_adbox_",
            "icon": "Project Wonderful.png",
            "script": "^https?://(?:www\\.)?projectwonderful\\.com/(?:pwa\\.js|gen\\.php)",
            "website": "projectwonderful.com"
        },
        "Prospector": {
            "cats": [
                36
            ],
            "html": "<[^>]+data-name=['\"]prospectscript",
            "icon": "Prospector.png",
            "script": "processprospector\\.js",
            "website": "prospector.io"
        },
        "Prototype": {
            "cats": [
                12
            ],
            "env": "^Prototype$",
            "icon": "Prototype.png",
            "script": "(?:prototype|protoaculous)(?:-([\\d.]*[\\d]))?.*\\.js\\;version:\\1",
            "website": "www.prototypejs.org"
        },
        "Protovis": {
            "cats": [
                25
            ],
            "env": "^protovis$",
            "icon": "default.png",
            "script": "protovis.*\\.js",
            "website": "mbostock.github.com/protovis"
        },
        "PubMatic": {
            "cats": [
                36
            ],
            "icon": "PubMatic.png",
            "script": "https?://[^/]*\\.pubmatic\\.com",
            "website": "www.pubmatic.com/"
        },
        "Public CMS": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "PUBLICCMS_USER",
                "X-Powered-PublicCMS": ""
            },
            "icon": "Public CMS.png",
            "implies": "Java",
            "website": "www.publiccms.com"
        },
        "Pure CSS": {
            "cats": [
                18
            ],
            "html": "<link[^>]+(?:([\\d.])+/)?pure(?:-min)?\\.css\\;version:\\1",
            "icon": "Pure CSS.png",
            "website": "purecss.io"
        },
        "PyroCMS": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "pyrocms",
                "X-Streams-Distribution": "PyroCMS"
            },
            "icon": "PyroCMS.png",
            "implies": "Laravel",
            "website": "pyrocms.com"
        },
        "Python": {
            "cats": [
                27
            ],
            "headers": {
                "Server": "(?:^|\\s)Python(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Python.png",
            "website": "python.org"
        },
        "Quantcast": {
            "cats": [
                10
            ],
            "env": "^quantserve$",
            "icon": "Quantcast.png",
            "script": "edge\\.quantserve\\.com/quant\\.js",
            "website": "www.quantcast.com"
        },
        "Question2Answer": {
            "cats": [
                15
            ],
            "html": "<!-- Powered by Question2Answer",
            "icon": "question2answer.png",
            "implies": "PHP",
            "script": "\\./qa-content/qa-page\\.js\\?([0-9.]+)\\;version:\\1",
            "website": "www.question2answer.org"
        },
        "Quick.CMS": {
            "cats": [
                1
            ],
            "html": "<a href=\"[^>]+opensolution\\.org/\">CMS by",
            "icon": "Quick.CMS.png",
            "meta": {
                "generator": "Quick\\.CMS(?: v([\\d.]+))?\\;version:\\1"
            },
            "website": "opensolution.org"
        },
        "Quick.Cart": {
            "cats": [
                6
            ],
            "html": "<a href=\"[^>]+opensolution\\.org/\">(?:Shopping cart by|Sklep internetowy)",
            "icon": "Quick.Cart.png",
            "meta": {
                "generator": "Quick\\.Cart(?: v([\\d.]+))?\\;version:\\1"
            },
            "website": "opensolution.org"
        },
        "Quill": {
            "cats": [
                24
            ],
            "env": "^Quill$",
            "icon": "Quill.png",
            "website": "quilljs.com"
        },
        "RAID HTTPServer": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "RAID HTTPServer(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "???"
        },
        "RBS Change": {
            "cats": [
                1,
                6
            ],
            "html": "<html[^>]+xmlns:change=",
            "icon": "RBS Change.png",
            "implies": "PHP",
            "meta": {
                "generator": "RBS Change"
            },
            "website": "www.rbschange.fr"
        },
        "RCMS": {
            "cats": [
                1
            ],
            "icon": "RCMS.png",
            "meta": {
                "generator": "^(?:RCMS|ReallyCMS)"
            },
            "website": "www.rcms.fi"
        },
        "RD Station": {
            "cats": [
                32
            ],
            "env": "^RDStation$",
            "icon": "RD Station.png",
            "script": "d335luupugsy2\\.cloudfront\\.net/js/loader-scripts/.*-loader\\.js",
            "website": "rdstation.com.br"
        },
        "RDoc": {
            "cats": [
                4
            ],
            "html": [
                "<link[^>]+href=\"[^\"]*rdoc-style\\.css",
                "Generated by <a[^>]+href=\"https?://rdoc\\.rubyforge\\.org[^>]+>RDoc</a> ([\\d.]*\\d)\\;version:\\1"
            ],
            "icon": "RDoc.png",
            "implies": "Ruby",
            "website": "github.com/RDoc/RDoc"
        },
        "RackCache": {
            "cats": [
                23
            ],
            "headers": {
                "X-Rack-Cache": ""
            },
            "icon": "RackCache.png",
            "implies": "Ruby",
            "website": "github.com/rtomayko/rack-cache"
        },
        "RainLoop": {
            "cats": [
                30
            ],
            "env": "^rainloop",
            "headers": {
                "Server": "RainLoop"
            },
            "html": [
                "<meta [^>]*(?:content=\"([^\"]+)[^>]+ id=\"rlAppVersion\"|id=\"rlAppVersion\"[^>]+ content=\"([^\"]+))\\;version:\\1?\\1:\\2",
                "<link[^>]* href=\"[^\"]*rainloop/v/([^/]+)\\;version:\\1"
            ],
            "icon": "RainLoop.png",
            "implies": "PHP",
            "script": "rainloop/v/([^/]+)\\;version:\\1",
            "website": "rainloop.net"
        },
        "Ramda": {
            "cats": [
                12
            ],
            "icon": "Ramda.png",
            "script": "ramda.*\\.js",
            "website": "ramdajs.com"
        },
        "Raphael": {
            "cats": [
                25
            ],
            "env": "^Raphael$",
            "icon": "Raphael.png",
            "script": "raphael.*\\.js",
            "website": "raphaeljs.com"
        },
        "Rapid Logic": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Rapid Logic(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "???"
        },
        "React": {
            "cats": [
                12
            ],
            "env": "^React$",
            "html": "<[^>]+data-react",
            "icon": "React.png",
            "script": [
                "react(?:\\-with\\-addons)?(?:\\-|\\.)([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
                "/([\\d.]+)/react(?:\\.min)?\\.js\\;version:\\1",
                "react.*\\.js"
            ],
            "website": "facebook.github.io/react"
        },
        "Red Hat": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "Red Hat",
                "X-Powered-By": "Red Hat"
            },
            "icon": "Red Hat.png",
            "website": "redhat.com"
        },
        "Reddit": {
            "cats": [
                2
            ],
            "env": "^reddit$",
            "html": "(?:<a[^>]+Powered by Reddit|powered by <a[^>]+>reddit<)",
            "icon": "Reddit.png",
            "implies": "Python",
            "url": "^(?:www\\.)?reddit\\.com",
            "website": "code.reddit.com"
        },
        "Redmine": {
            "cats": [
                13
            ],
            "html": "Powered by <a href=\"[^>]+Redmine",
            "icon": "Redmine.png",
            "implies": "Ruby on Rails",
            "meta": {
                "description": "Redmine"
            },
            "website": "www.redmine.org"
        },
        "Reinvigorate": {
            "cats": [
                10
            ],
            "env": "^reinvigorate$",
            "icon": "Reinvigorate.png",
            "website": "www.reinvigorate.net"
        },
        "RequireJS": {
            "cats": [
                12
            ],
            "env": "^requirejs$",
            "icon": "RequireJS.png",
            "script": "require.*\\.js",
            "website": "requirejs.org"
        },
        "Resin": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "^Resin(?:/(\\S*))?\\;version:\\1"
            },
            "icon": "Resin.png",
            "implies": "Java",
            "website": "caucho.com"
        },
        "Reveal.js": {
            "cats": [
                12
            ],
            "env": "^Reveal$",
            "icon": "Reveal.js.png",
            "script": "reveal(?:\\.min)?\\.js",
            "website": "lab.hakim.se/reveal-js"
        },
        "Rickshaw": {
            "cats": [
                25
            ],
            "env": "^Rickshaw$",
            "icon": "default.png",
            "implies": "D3",
            "script": "rickshaw(?:\\.min)?\\.js",
            "website": "code.shutterstock.com/rickshaw/"
        },
        "RightJS": {
            "cats": [
                12
            ],
            "env": "^RightJS$",
            "icon": "RightJS.png",
            "script": "right\\.js",
            "website": "rightjs.org"
        },
        "Riot": {
            "cats": [
                12
            ],
            "env": "^riot$",
            "icon": "Riot.png",
            "script": "riot(?:\\+compiler)?(?:\\.min)?\\.js",
            "website": "muut.com/riotjs"
        },
        "RiteCMS": {
            "cats": [
                1
            ],
            "icon": "RiteCMS.png",
            "implies": [
                "PHP",
                "SQLite"
            ],
            "meta": {
                "generator": "^RiteCMS(?: (.+))?\\;version:\\1"
            },
            "website": "ritecms.com"
        },
        "Roadiz CMS": {
            "cats": [
                1,
                11
            ],
            "icon": "Roadiz CMS.png",
            "implies": "PHP",
            "meta": {
                "generator": "^Roadiz ([a-z0-9\\s\\.]+) - \\;version:\\1"
            },
            "website": "www.roadiz.io"
        },
        "Robin": {
            "cats": [
                6
            ],
            "env": [
                "_robin_getRobinJs",
                "robin_settings",
                "robin_storage_settings"
            ],
            "icon": "Robin.png",
            "website": "www.robinhq.com"
        },
        "RoundCube": {
            "cats": [
                30
            ],
            "env": "^(?:rcmail|rcube_|roundcube)",
            "html": "<title>RoundCube",
            "icon": "RoundCube.png",
            "implies": "PHP",
            "website": "roundcube.net"
        },
        "Rubicon Project": {
            "cats": [
                36
            ],
            "icon": "Rubicon Project.png",
            "script": "https?://[^/]*\\.rubiconproject\\.com",
            "website": "rubiconproject.com/"
        },
        "Ruby": {
            "cats": [
                27
            ],
            "headers": {
                "Server": "(?:Mongrel|WEBrick|Ruby)"
            },
            "icon": "Ruby.png",
            "website": "ruby-lang.org"
        },
        "Ruby on Rails": {
            "cats": [
                18
            ],
            "headers": {
                "Server": "(?:mod_rails|mod_rack|Phusion(?:\\.|_)Passenger)",
                "X-Powered-By": "(?:mod_rails|mod_rack|Phusion[\\._ ]Passenger)(?: \\(mod_rails/mod_rack\\))?(?: ?/?([\\d\\.]+))?\\;version:\\1"
            },
            "icon": "Ruby on Rails.png",
            "implies": "Ruby",
            "meta": {
                "csrf-param": "authenticity_token"
            },
            "script": "/assets/application-[a-z\\d]{32}/\\.js",
            "website": "rubyonrails.org"
        },
        "Ruxit": {
            "cats": [
                10
            ],
            "icon": "Ruxit.png",
            "script": "ruxitagentjs",
            "website": "ruxit.com"
        },
        "RxJS": {
            "cats": [
                12
            ],
            "env": "^Rx$",
            "icon": "RxJS.png",
            "script": "rx(?:\\.\\w+)?(?:\\.compat)?(?:\\.min)?\\.js",
            "website": "reactivex.io"
        },
        "S.Builder": {
            "cats": [
                1
            ],
            "icon": "S.Builder.png",
            "meta": {
                "generator": "S\\.Builder"
            },
            "website": "www.sbuilder.ru"
        },
        "SAP": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "SAP NetWeaver Application Server"
            },
            "icon": "SAP.png",
            "website": "sap.com"
        },
        "SDL Tridion": {
            "cats": [
                1
            ],
            "html": "<img[^>]+_tcm\\d{2,3}-\\d{6}\\.",
            "icon": "SDL Tridion.png",
            "website": "www.sdl.com/products/tridion"
        },
        "SIMsite": {
            "cats": [
                1
            ],
            "icon": "SIMsite.png",
            "meta": {
                "SIM.medium": ""
            },
            "script": "/sim(?:site|core)/js",
            "website": "simgroep.nl/internet/portfolio-contentbeheer_41623/"
        },
        "SMF": {
            "cats": [
                2
            ],
            "env": "^smf_",
            "icon": "SMF.png",
            "implies": "PHP",
            "website": "www.simplemachines.org"
        },
        "SOBI 2": {
            "cats": [
                19
            ],
            "html": "(?:<!-- start of Sigsiu Online Business Index|<div[^>]* class=\"sobi2)",
            "icon": "SOBI 2.png",
            "implies": "Joomla",
            "website": "www.sigsiu.net/sobi2.html"
        },
        "SPDY": {
            "cats": [
                19
            ],
            "excludes": "HTTP/2",
            "headers": {
                "X-Firefox-Spdy": "\\d\\.\\d"
            },
            "icon": "SPDY.png",
            "website": "chromium.org/spdy"
        },
        "SPIP": {
            "cats": [
                1
            ],
            "headers": {
                "X-Spip-Cache": ""
            },
            "icon": "SPIP.png",
            "meta": {
                "generator": "(?:^|\\s)SPIP(?:\\s([\\d.]+(?:\\s\\[\\d+\\])?))?\\;version:\\1"
            },
            "website": "www.spip.net"
        },
        "SQL Buddy": {
            "cats": [
                3
            ],
            "html": "(?:<title>SQL Buddy</title>|<[^>]+onclick=\"sideMainClick\\(\"home\\.php)",
            "icon": "SQL Buddy.png",
            "website": "www.sqlbuddy.com"
        },
        "SQLite": {
            "cats": [
                34
            ],
            "icon": "SQLite.png",
            "website": "www.sqlite.org"
        },
        "SUSE": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "SUSE(?:/?\\s?-?([\\d.]+))?\\;version:\\1",
                "X-Powered-By": "SUSE(?:/?\\s?-?([\\d.]+))?\\;version:\\1"
            },
            "icon": "SUSE.png",
            "website": "suse.com"
        },
        "SWFObject": {
            "cats": [
                19
            ],
            "env": "^SWFObject$",
            "icon": "SWFObject.png",
            "script": "swfobject.*\\.js",
            "website": "github.com/swfobject/swfobject"
        },
        "Saia PCD": {
            "cats": [
                45
            ],
            "headers": {
                "Server": "Saia PCD(?:([/a-z\\d.]+))?\\;version:\\1"
            },
            "icon": "Saia PCD.png",
            "website": "saia-pcd.com"
        },
        "Sails.js": {
            "cats": [
                18
            ],
            "headers": {
                "Set-Cookie": "^sails\\.sid$",
                "X-Powered-By": "^Sails$"
            },
            "icon": "Sails.js.svg",
            "implies": [
                "Node.js",
                "Express"
            ],
            "website": "sailsjs.org"
        },
        "Sarka-SPIP": {
            "cats": [
                1
            ],
            "icon": "Sarka-SPIP.png",
            "implies": "SPIP",
            "meta": {
                "generator": "Sarka-SPIP(?:\\s([\\d.]+))?\\;version:\\1"
            },
            "website": "sarka-spip.net"
        },
        "Scala": {
            "cats": [
                27
            ],
            "icon": "Scala.png",
            "website": "www.scala-lang.org"
        },
        "Schneider": {
            "cats": [
                45
            ],
            "icon": "Schneider.png",
            "website": "schneider-electric.com"
        },
        "Schneider Web Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Schneider-WEB(?:/V?([\\d.]+))?\\;version:\\1"
            },
            "icon": "Schneider Web Server.png",
            "implies": [
                "Schneider"
            ],
            "website": "schneider-electric.com"
        },
        "Scientific Linux": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "Scientific Linux",
                "X-Powered-By": "Scientific Linux"
            },
            "icon": "Scientific Linux.png",
            "website": "scientificlinux.org"
        },
        "Segment": {
            "cats": [
                10
            ],
            "env": "^analytics$",
            "html": "<script[\\s\\S]*cdn\\.segment\\.com/analytics.js[\\s\\S]*script>",
            "icon": "Segment.png",
            "script": "cdn\\.segment\\.com/analytics\\.js",
            "website": "segment.com"
        },
        "Select2": {
            "cats": [
                12
            ],
            "icon": "default.png",
            "implies": "jQuery",
            "script": "select2.*\\.js",
            "website": "select2.github.io"
        },
        "Semantic-ui": {
            "cats": [
                18
            ],
            "html": [
                "(?:<div class=\"ui\\s[^>]+\">)",
                "(?:<link[^>]+semantic(?:\\.css|\\.min\\.css)\">)"
            ],
            "icon": "Semantic-ui.png",
            "script": "(?:semantic(?:\\.js|\\.min\\.js))",
            "website": "semantic-ui.com"
        },
        "Sencha Touch": {
            "cats": [
                12,
                26
            ],
            "icon": "Sencha Touch.png",
            "script": "sencha-touch.*\\.js",
            "website": "sencha.com/products/touch"
        },
        "Sentinel Keys Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "SentinelKeysServer\\/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "Sentinel Keys Server.png",
            "website": "www.safenet-inc.com/software-monetization/sentinel-rms"
        },
        "Sentinel License Monitor": {
            "cats": [
                19
            ],
            "html": "<title>Sentinel (?:Keys )?License Monitor</title>",
            "icon": "Sentinel License Monitor.png",
            "website": "www.safenet-inc.com/software-monetization/sentinel-rms/"
        },
        "Sentinel Protection Server": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "SentinelProtectionServer\\/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "Sentinel Protection Server.png",
            "website": "www.safenet-inc.com/software-monetization/sentinel-rms/"
        },
        "Serendipity": {
            "cats": [
                1,
                11
            ],
            "icon": "Serendipity.png",
            "implies": "PHP",
            "meta": {
                "Powered-By": "Serendipity v\\.(.+)\\;version:\\1",
                "generator": "Serendipity"
            },
            "website": "s9y.org"
        },
        "Shadow": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "ShadowFramework"
            },
            "icon": "Shadow.png",
            "implies": "PHP",
            "website": "shadow-technologies.co.uk"
        },
        "ShareThis": {
            "cats": [
                5
            ],
            "env": "^SHARETHIS$",
            "icon": "ShareThis.png",
            "script": "w\\.sharethis\\.com/",
            "website": "sharethis.com"
        },
        "ShinyStat": {
            "cats": [
                10
            ],
            "env": "^SSsdk$",
            "html": "<img[^>]*\\s+src=['\"]?https?://www\\.shinystat\\.com/cgi-bin/shinystat\\.cgi\\?[^'\"\\s>]*['\"\\s/>]",
            "icon": "ShinyStat.png",
            "script": "^https?://codice(?:business|ssl|pro|isp)?\\.shinystat\\.com/cgi-bin/getcod\\.cgi",
            "website": "shinystat.com"
        },
        "Shopalize": {
            "cats": [
                5,
                10
            ],
            "env": "^Shopalize$",
            "icon": "Shopalize.png",
            "website": "shopalize.com"
        },
        "Shopatron": {
            "cats": [
                6
            ],
            "env": "^shptUrl$",
            "html": [
                "<body class=\"shopatron",
                "<img[^>]+mediacdn\\.shopatron\\.com"
            ],
            "icon": "Shopatron.png",
            "meta": {
                "keywords": "Shopatron"
            },
            "script": "mediacdn\\.shopatron\\.com",
            "website": "ecommerce.shopatron.com"
        },
        "Shopery": {
            "cats": [
                6
            ],
            "headers": {
                "X-Shopery": ""
            },
            "icon": "Shopery.svg",
            "implies": [
                "PHP",
                "Symfony",
                "Elcodi"
            ],
            "website": "shopery.com"
        },
        "Shopify": {
            "cats": [
                6
            ],
            "env": "^Shopify$",
            "html": "<link[^>]+=['\"]//cdn\\.shopify\\.com",
            "icon": "Shopify.svg",
            "website": "shopify.com"
        },
        "Shoptet": {
            "cats": [
                6
            ],
            "env": "^shoptet$",
            "html": "<link [^>]*href=\"https?://cdn\\.myshoptet\\.com/",
            "icon": "Shoptet.svg",
            "implies": "PHP",
            "meta": {
                "web_author": "^Shoptet"
            },
            "script": [
                "^https?://cdn\\.myshoptet\\.com/"
            ],
            "website": "www.shoptet.cz"
        },
        "Shopware": {
            "cats": [
                6
            ],
            "html": "<title>Shopware ([\\d\\.]+) [^<]+\\;version:\\1",
            "icon": "Shopware.png",
            "implies": [
                "PHP",
                "MySQL",
                "jQuery"
            ],
            "meta": {
                "application-name": "Shopware"
            },
            "script": "(?:(shopware)|/web/cache/[0-9]{10}_.+)\\.js\\;version:\\1?4:5",
            "website": "shopware.com"
        },
        "Silva": {
            "cats": [
                1
            ],
            "headers": {
                "X-Powered-By": "SilvaCMS"
            },
            "icon": "Silva.png",
            "website": "silvacms.org"
        },
        "SilverStripe": {
            "cats": [
                1
            ],
            "html": "Powered by <a href=\"[^>]+SilverStripe",
            "icon": "SilverStripe.svg",
            "meta": {
                "generator": "SilverStripe"
            },
            "website": "www.silverstripe.org"
        },
        "SimpleHTTP": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "SimpleHTTP(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "???"
        },
        "Site Meter": {
            "cats": [
                10
            ],
            "icon": "Site Meter.png",
            "script": "sitemeter\\.com/js/counter\\.js\\?site=",
            "website": "www.sitemeter.com"
        },
        "SiteCatalyst": {
            "cats": [
                10
            ],
            "env": "^s_(?:account|objectID|code|INST)$",
            "icon": "SiteCatalyst.png",
            "script": "/s[_-]code.*\\.js",
            "website": "www.adobe.com/solutions/digital-marketing.html"
        },
        "SiteEdit": {
            "cats": [
                1
            ],
            "icon": "SiteEdit.png",
            "meta": {
                "generator": "SiteEdit"
            },
            "website": "www.siteedit.ru"
        },
        "Sitecore": {
            "cats": [
                1
            ],
            "headers": {
                "Set-cookie": "SC_ANALYTICS_GLOBAL_COOKIE"
            },
            "html": "<img[^>]+src=\"[^>]*/~/media/[^>]+\\.ashx",
            "icon": "Sitecore.png",
            "website": "sitecore.net"
        },
        "Sivuviidakko": {
            "cats": [
                1
            ],
            "icon": "Sivuviidakko.png",
            "meta": {
                "generator": "Sivuviidakko"
            },
            "website": "sivuviidakko.fi"
        },
        "Sizmek": {
            "cats": [
                36
            ],
            "html": "(?:<a [^>]*href=\"[^/]*//[^/]*serving-sys\\.com/|<img [^>]*src=\"[^/]*//[^/]*serving-sys\\.com/)",
            "icon": "Sizmek.png",
            "script": "[^/]*//[^/]*serving-sys\\.com/",
            "website": "sizmek.com"
        },
        "Slimbox": {
            "cats": [
                7,
                12
            ],
            "html": "<link [^>]*href=\"[^/]*slimbox(?:-rtl)?\\.css",
            "icon": "Slimbox.png",
            "implies": "MooTools",
            "script": "slimbox\\.js",
            "website": "www.digitalia.be/software/slimbox"
        },
        "Slimbox 2": {
            "cats": [
                7,
                12
            ],
            "html": "<link [^>]*href=\"[^/]*slimbox2(?:-rtl)?\\.css",
            "icon": "Slimbox 2.png",
            "implies": "jQuery",
            "script": "slimbox2\\.js",
            "website": "www.digitalia.be/software/slimbox2"
        },
        "Smart Ad Server": {
            "cats": [
                36
            ],
            "env": "^SmartAdServer$",
            "html": "<img[^>]+smartadserver\\.com\\/call",
            "icon": "Smart Ad Server.png",
            "website": "smartadserver.com"
        },
        "SmartSite": {
            "cats": [
                1
            ],
            "html": "<[^>]+/smartsite\\.(?:dws|shtml)\\?id=",
            "icon": "SmartSite.png",
            "meta": {
                "author": "Redacteur SmartInstant"
            },
            "website": "www.seneca.nl/pub/Smartsite/Smartsite-Smartsite-iXperion"
        },
        "Smartstore": {
            "cats": [
                6
            ],
            "icon": "Smartstore.png",
            "script": "smjslib\\.js",
            "website": "smartstore.com"
        },
        "Snap": {
            "cats": [
                18,
                22
            ],
            "headers": {
                "Server": "Snap/([.\\d]+)\\;version:\\1"
            },
            "icon": "Snap.png",
            "implies": "Haskell",
            "website": "snapframework.com"
        },
        "Snap.svg": {
            "cats": [
                12
            ],
            "env": "^Snap$",
            "icon": "Snap.svg.png",
            "script": "snap\\.svg(?:-min)?\\.js",
            "website": "snapsvg.io"
        },
        "Snoobi": {
            "cats": [
                10
            ],
            "env": "^snoobi$",
            "icon": "Snoobi.png",
            "script": "snoobi\\.com/snoop\\.php",
            "website": "www.snoobi.com"
        },
        "SobiPro": {
            "cats": [
                19
            ],
            "env": "^SobiProUrl$",
            "icon": "SobiPro.png",
            "implies": "Joomla",
            "website": "sigsiu.net/sobipro.html"
        },
        "Socket.io": {
            "cats": [
                12
            ],
            "env": "^io$",
            "icon": "Socket.io.png",
            "implies": "Node.js",
            "script": "socket.io.*\\.js",
            "website": "socket.io"
        },
        "Solodev": {
            "cats": [
                1
            ],
            "headers": {
                "solodev_session": ""
            },
            "html": "<div class='dynamicDiv' id='dd\\.\\d\\.\\d'>",
            "icon": "Solodev.png",
            "implies": "PHP",
            "website": "www.solodev.com"
        },
        "Solr": {
            "cats": [
                34
            ],
            "icon": "Solr.png",
            "implies": "Lucene",
            "website": "lucene.apache.org/solr/"
        },
        "Solve Media": {
            "cats": [
                16,
                36
            ],
            "env": "^(?:_?ACPuzzle|adcopy-puzzle-image-image$)",
            "icon": "Solve Media.png",
            "script": "^https?://api\\.solvemedia\\.com/",
            "website": "solvemedia.com"
        },
        "SoundManager": {
            "cats": [
                12
            ],
            "env": "^(?:SoundManager|BaconPlayer)$",
            "icon": "SoundManager.png",
            "website": "www.schillmania.com/projects/soundmanager2"
        },
        "Sphinx": {
            "cats": [
                4
            ],
            "env": "^DOCUMENTATION_OPTIONS$",
            "icon": "Sphinx.png",
            "implies": "Python",
            "website": "sphinx.pocoo.org"
        },
        "SpiderControl iniNet": {
            "cats": [
                45
            ],
            "icon": "SpiderControl iniNet.png",
            "meta": {
                "generator": "iniNet SpiderControl"
            },
            "website": "spidercontrol.net/ininet"
        },
        "Splunk": {
            "cats": [
                19
            ],
            "html": "<p class=\"footer\">&copy; [-\\d]+ Splunk Inc\\.(?: Splunk ([\\d\\.]+(?: build [\\d\\.]*\\d)?))?[^<]*</p>\\;version:\\1",
            "icon": "Splunk.png",
            "meta": {
                "author": "Splunk Inc"
            },
            "website": "splunk.com"
        },
        "Splunkd": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Splunkd"
            },
            "icon": "Splunkd.png",
            "website": "splunk.com"
        },
        "Spree": {
            "cats": [
                6
            ],
            "html": "(?:<link[^>]*/assets/store/all-[a-z\\d]{32}\\.css[^>]+>|<script>\\s*Spree\\.(?:routes|translations|api_key))",
            "icon": "Spree.png",
            "implies": "Ruby on Rails",
            "website": "spreecommerce.com"
        },
        "Squarespace": {
            "cats": [
                1
            ],
            "env": "^Squarespace",
            "headers": {
                "X-ServedBy": "squarespace"
            },
            "icon": "Squarespace.png",
            "website": "www.squarespace.com"
        },
        "SquirrelMail": {
            "cats": [
                30
            ],
            "env": "^squirrelmail_loginpage_onload$",
            "html": "<small>SquirrelMail version ([.\\d]+)[^<]*<br \\;version:\\1",
            "icon": "SquirrelMail.png",
            "implies": "PHP",
            "url": "/src/webmail\\.php(?:$|\\?)",
            "website": "squirrelmail.org"
        },
        "Squiz Matrix": {
            "cats": [
                1
            ],
            "headers": {
                "X-Powered-By": "Squiz Matrix"
            },
            "html": "<!--\\s+Running (?:MySource|Squiz) Matrix",
            "icon": "Squiz Matrix.png",
            "implies": "PHP",
            "meta": {
                "generator": "Squiz Matrix"
            },
            "website": "squiz.net"
        },
        "Stackla": {
            "cats": [
                5
            ],
            "env": "^Stackla$",
            "icon": "Stackla.png",
            "script": "assetscdn\\.stackla\\.com\\/media\\/js\\/widget\\/(?:[a-zA-Z0-9.]+)?\\.js",
            "website": "stackla.com/"
        },
        "Stackla Social Hub": {
            "cats": [
                1
            ],
            "env": "^stacklaSocialHub$",
            "icon": "Stackla Social Hub.png",
            "website": "stackla.com/"
        },
        "Stamplay": {
            "cats": [
                34,
                47
            ],
            "headers": {
                "Server": "Stamplay"
            },
            "icon": "Stamplay.png",
            "script": "stamplay.*\\.js",
            "website": "stamplay.com"
        },
        "Starlet": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "^Plack::Handler::Starlet"
            },
            "icon": "Starlet.png",
            "implies": "Perl",
            "website": "metacpan.org/pod/Starlet"
        },
        "StatCounter": {
            "cats": [
                10
            ],
            "icon": "StatCounter.png",
            "script": "statcounter\\.com/counter/counter",
            "website": "www.statcounter.com"
        },
        "Store Systems": {
            "cats": [
                6
            ],
            "html": "Shopsystem von <a href=[^>]+store-systems\\.de\"|\\.mws_boxTop",
            "icon": "Store Systems.png",
            "website": "store-systems.de"
        },
        "Strapdown.js": {
            "cats": [
                12
            ],
            "icon": "strapdown.js.png",
            "implies": [
                "Twitter Bootstrap",
                "Google Code Prettify"
            ],
            "script": "strapdown\\.js",
            "website": "strapdownjs.com"
        },
        "Strato": {
            "cats": [
                6
            ],
            "html": "<a href=\"http://www.strato.de/\" target=\"_blank\">",
            "icon": "strato.png",
            "website": "shop.strato.com"
        },
        "Stripe": {
            "cats": [
                41
            ],
            "env": "^Stripe$",
            "html": "<input[^>]+data-stripe",
            "icon": "Stripe.png",
            "script": "js\\.stripe\\.com",
            "website": "stripe.com"
        },
        "SublimeVideo": {
            "cats": [
                14
            ],
            "env": "^sublimevideo$",
            "icon": "SublimeVideo.png",
            "script": "cdn\\.sublimevideo\\.net/js/[a-z\\d]+\\.js",
            "website": "sublimevideo.net"
        },
        "Subrion": {
            "cats": [
                1
            ],
            "headers": {
                "X-Powered-CMS": "Subrion CMS"
            },
            "icon": "Subrion.png",
            "implies": "PHP",
            "meta": {
                "generator": "^Subrion "
            },
            "website": "subrion.com"
        },
        "Sulu": {
            "cats": [
                1
            ],
            "headers": {
                "X-Generator": "Sulu/?(.+)?$\\;version:\\1"
            },
            "icon": "Sulu.svg",
            "implies": [
                "PHP",
                "Symfony"
            ],
            "website": "sulu.io"
        },
        "SumoMe": {
            "cats": [
                5,
                10,
                32,
                36,
                47,
                51
            ],
            "icon": "SumoMe.png",
            "script": "load\\.sumome\\.com",
            "website": "sumome.com"
        },
        "SunOS": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "SunOS( [\\d\\.]+)?\\;version:\\1",
                "Servlet-engine": "SunOS( [\\d\\.]+)?\\;version:\\1"
            },
            "icon": "Oracle.png",
            "website": "oracle.com/solaris"
        },
        "Supersized": {
            "cats": [
                7,
                25
            ],
            "icon": "Supersized.png",
            "script": "supersized(?:\\.([\\d.]*[\\d]))?.*\\.js\\;version:\\1",
            "website": "buildinternet.com/project/supersized"
        },
        "SweetAlert": {
            "cats": [
                12
            ],
            "env": "^swal$",
            "html": "<link[^>]+?href=\"[^\"]+sweet-alert(?:\\.min)?\\.css",
            "icon": "SweetAlert.png",
            "script": "sweet-alert(?:\\.min)?\\.js",
            "website": "tristanedwards.me/sweetalert"
        },
        "Swiftlet": {
            "cats": [
                18
            ],
            "headers": {
                "X-Generator": "Swiftlet",
                "X-Powered-By": "Swiftlet",
                "X-Swiftlet-Cache": ""
            },
            "html": "Powered by <a href=\"[^>]+Swiftlet",
            "icon": "Swiftlet.png",
            "implies": "PHP",
            "meta": {
                "generator": "Swiftlet"
            },
            "website": "swiftlet.org"
        },
        "Symfony": {
            "cats": [
                18
            ],
            "icon": "Symfony.png",
            "implies": "PHP",
            "website": "symfony.com"
        },
        "Synology DiskStation": {
            "cats": [
                48
            ],
            "icon": "Synology DiskStation.png",
            "meta": {
                "application-name": "Synology DiskStation"
            },
            "website": "synology.com"
        },
        "SyntaxHighlighter": {
            "cats": [
                19
            ],
            "env": "^SyntaxHighlighter$",
            "html": "<(?:script|link)[^>]*sh(?:Core|Brush|ThemeDefault)",
            "icon": "SyntaxHighlighter.png",
            "website": "github.com/syntaxhighlighter"
        },
        "TWiki": {
            "cats": [
                8
            ],
            "headers": {
                "Set-cookie": "TWIKISID"
            },
            "html": "<img [^>]*(?:title|alt)=\"This site is powered by the TWiki collaboration platform",
            "icon": "TWiki.png",
            "script": "(?:TWikiJavascripts|twikilib(?:\\.min)?\\.js)",
            "website": "twiki.org"
        },
        "TYPO3 CMS": {
            "cats": [
                1
            ],
            "html": "<(?:script[^>]+ src|link[^>]+ href)=[^>]+typo3temp/",
            "icon": "TYPO3.svg",
            "implies": "PHP",
            "meta": {
                "generator": "TYPO3\\s+(?:CMS\\s+)?([\\d.]+)?(?:\\s+CMS)?\\;version:\\1"
            },
            "url": "/typo3/",
            "website": "www.typo3.org"
        },
        "TYPO3 Flow": {
            "cats": [
                18
            ],
            "excludes": "TYPO3 CMS",
            "headers": {
                "X-Flow-Powered": "Flow/?(.+)?$\\;version:\\1"
            },
            "icon": "TYPO3.svg",
            "implies": "PHP",
            "website": "flow.typo3.org"
        },
        "TYPO3 Neos": {
            "cats": [
                1
            ],
            "excludes": "TYPO3 CMS",
            "html": "<html[^>]+xmlns:typo3=\"[^\"]+Flow/Packages/Neos/",
            "icon": "TYPO3.svg",
            "implies": [
                "PHP",
                "TYPO3 Flow"
            ],
            "url": "/neos/",
            "website": "neos.io"
        },
        "Taiga": {
            "cats": [
                13
            ],
            "env": "^taigaConfig$",
            "icon": "Taiga.png",
            "implies": [
                "Django",
                "AngularJS"
            ],
            "website": "taiga.io"
        },
        "Tealeaf": {
            "cats": [
                10
            ],
            "env": "^TeaLeaf$",
            "icon": "Tealeaf.png",
            "website": "www.tealeaf.com"
        },
        "TeamCity": {
            "cats": [
                44
            ],
            "html": "<span class=\"versionTag\"><span class=\"vWord\">Version</span> ([\\d\\.]+)\\;version:\\1",
            "icon": "TeamCity.png",
            "implies": [
                "jQuery",
                "Prototype"
            ],
            "meta": {
                "application-name": "TeamCity"
            },
            "website": "jetbrains.com/teamcity"
        },
        "Telescope": {
            "cats": [
                1
            ],
            "env": "Telescope",
            "icon": "Telescope.png",
            "implies": "Meteor",
            "website": "telescopeapp.org"
        },
        "Tengine": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Tengine"
            },
            "icon": "Tengine.png",
            "website": "tengine.taobao.org"
        },
        "Textpattern CMS": {
            "cats": [
                1
            ],
            "icon": "Textpattern CMS.png",
            "meta": {
                "generator": "Textpattern"
            },
            "website": "textpattern.com"
        },
        "Thelia": {
            "cats": [
                1,
                6
            ],
            "html": "<(?:link|style|script)[^>]+/assets/frontOffice/",
            "icon": "Thelia.png",
            "implies": [
                "PHP",
                "Symfony"
            ],
            "website": "thelia.net"
        },
        "ThinkPHP": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "ThinkPHP"
            },
            "icon": "ThinkPHP.png",
            "implies": "PHP",
            "website": "www.thinkphp.cn"
        },
        "TiddlyWiki": {
            "cats": [
                1,
                2,
                4,
                8
            ],
            "env": "tiddler",
            "html": "<[^>]*type=[^>]text\\/vnd\\.tiddlywiki",
            "icon": "TiddlyWiki.png",
            "meta": {
                "application-name": "^TiddlyWiki$",
                "copyright": "^TiddlyWiki created by Jeremy Ruston",
                "generator": "^TiddlyWiki$",
                "tiddlywiki-version": "(.*)\\;version:\\1"
            },
            "website": "tiddlywiki.com"
        },
        "Tiki Wiki CMS Groupware": {
            "cats": [
                1,
                2,
                8,
                11,
                13
            ],
            "icon": "Tiki Wiki CMS Groupware.png",
            "meta": {
                "generator": "^Tiki"
            },
            "script": "(?:/|_)tiki",
            "website": "tiki.org"
        },
        "Timeplot": {
            "cats": [
                25
            ],
            "env": "^Timeplot$",
            "icon": "Timeplot.png",
            "script": "timeplot.*\\.js",
            "website": "www.simile-widgets.org/timeplot/"
        },
        "TinyMCE": {
            "cats": [
                24
            ],
            "env": "^tinyMCE$",
            "icon": "TinyMCE.png",
            "website": "tinymce.com"
        },
        "Titan": {
            "cats": [
                36
            ],
            "env": [
                "^titan$",
                "^titanEnabled$"
            ],
            "html": "<script[^>]+>var titan",
            "icon": "Titan.png",
            "website": "titan360.com"
        },
        "TomatoCart": {
            "cats": [
                6
            ],
            "env": "^AjaxShoppingCart$",
            "icon": "TomatoCart.png",
            "meta": {
                "generator": "TomatoCart"
            },
            "website": "tomatocart.com"
        },
        "TornadoServer": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "TornadoServer(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "TornadoServer.png",
            "website": "tornadoweb.org"
        },
        "Trac": {
            "cats": [
                13
            ],
            "html": [
                "<a id=\"tracpowered",
                "Powered by <a href=\"[^\"]*\"><strong>Trac(?:[ /]([\\d.]+))?\\;version:\\1"
            ],
            "icon": "Trac.png",
            "implies": "Python",
            "website": "trac.edgewall.org"
        },
        "TrackJs": {
            "cats": [
                10
            ],
            "env": "^TrackJs$",
            "icon": "TrackJs.png",
            "script": "tracker.js",
            "website": "trackjs.com"
        },
        "Tumblr": {
            "cats": [
                11
            ],
            "headers": {
                "X-Tumblr-User": ""
            },
            "html": "<iframe src=\"[^>]+tumblr\\.com",
            "icon": "Tumblr.png",
            "url": "^https?://(?:www\\.)?[^/]+\\.tumblr\\.com/",
            "website": "www.tumblr.com"
        },
        "TweenMax": {
            "cats": [
                12
            ],
            "env": "^TweenMax$",
            "icon": "TweenMax.png",
            "script": "TweenMax(?:\\.min)?\\.js",
            "website": "greensock.com/tweenmax"
        },
        "Twilight CMS": {
            "cats": [
                1
            ],
            "headers": {
                "X-Powered-CMS": "Twilight CMS"
            },
            "icon": "Twilight CMS.png",
            "website": "www.twilightcms.com"
        },
        "TwistPHP": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "TwistPHP"
            },
            "icon": "TwistPHP.png",
            "implies": "PHP",
            "website": "twistphp.com"
        },
        "TwistedWeb": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "TwistedWeb(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "TwistedWeb.png",
            "website": "twistedmatrix.com/trac/wiki/TwistedWeb"
        },
        "Twitter Bootstrap": {
            "cats": [
                18
            ],
            "env": "^Twipsy$",
            "html": [
                "<style>/\\*!\\* Bootstrap v(\\d\\.\\d\\.\\d)\\;version:\\1",
                "<link[^>]+?href=\"[^\"]+bootstrap(?:\\.min)?\\.css",
                "<div [^>]*class=\"[^\"]*col-(?:xs|sm|md|lg)-\\d{1,2}"
            ],
            "icon": "Twitter Bootstrap.png",
            "script": "(?:twitter\\.github\\.com/bootstrap|bootstrap(?:\\.js|\\.min\\.js))",
            "website": "getbootstrap.com"
        },
        "Twitter Emoji (Twemoji)": {
            "cats": [
                25
            ],
            "env": "^twemoji$",
            "icon": "default.png",
            "script": "twemoji(?:\\.min)?\\.js",
            "website": "twitter.github.io/twemoji/"
        },
        "Twitter Flight": {
            "cats": [
                12
            ],
            "env": "^flight$",
            "icon": "Twitter Flight.png",
            "implies": "jQuery",
            "website": "flightjs.github.io/"
        },
        "Twitter typeahead.js": {
            "cats": [
                12
            ],
            "env": "^typeahead$",
            "icon": "Twitter typeahead.js.png",
            "implies": "jQuery",
            "script": "(?:typeahead|bloodhound)\\.(?:jquery|bundle)?(?:\\.min)?\\.js",
            "website": "twitter.github.io/typeahead.js"
        },
        "TypePad": {
            "cats": [
                11
            ],
            "icon": "TypePad.png",
            "meta": {
                "generator": "typepad"
            },
            "url": "typepad\\.com",
            "website": "www.typepad.com"
        },
        "Typekit": {
            "cats": [
                17
            ],
            "env": "^Typekit$",
            "icon": "Typekit.png",
            "script": "use\\.typekit\\.com",
            "website": "typekit.com"
        },
        "UIKit": {
            "cats": [
                18
            ],
            "icon": "UIKit.png",
            "script": "uikit.*\\.js",
            "website": "getuikit.com"
        },
        "UNIX": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "Unix"
            },
            "icon": "UNIX.png",
            "website": "unix.org"
        },
        "Ubercart": {
            "cats": [
                6
            ],
            "icon": "Ubercart.png",
            "implies": "Drupal",
            "script": "uc_cart/uc_cart_block\\.js",
            "website": "www.ubercart.org"
        },
        "Ubuntu": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "Ubuntu",
                "X-Powered-By": "Ubuntu"
            },
            "icon": "Ubuntu.png",
            "website": "www.ubuntu.com/server"
        },
        "UltraCart": {
            "cats": [
                6
            ],
            "env": "^ucCatalog",
            "html": "<form [^>]*action=\"[^\"]*\\/cgi-bin\\/UCEditor\\?(?:[^\"]*&)?merchantId=[^\"]",
            "icon": "UltraCart.png",
            "script": "cgi-bin\\/UCJavaScript\\?(?:[^\"]*&)?merchantid=.",
            "url": "/cgi-bin/UCEditor\\?(?:.*&)?merchantid=.",
            "website": "ultracart.com"
        },
        "Umbraco": {
            "cats": [
                1
            ],
            "env": "^(?:UC_(?:IMAGE_SERVICE|ITEM_INFO_SERVICE|SETTINGS)|Umbraco)$",
            "headers": {
                "X-Umbraco-Version": "(.*)\\;version:\\1"
            },
            "html": "powered by <a href=[^>]+umbraco",
            "icon": "Umbraco.png",
            "implies": "Microsoft ASP.NET",
            "meta": {
                "generator": "umbraco"
            },
            "url": "/umbraco/login\\.aspx(?:$|\\?)",
            "website": "umbraco.com"
        },
        "Unbounce": {
            "cats": [
                20,
                51
            ],
            "headers": {
                "X-Unbounce-PageId": ""
            },
            "icon": "Unbounce.png",
            "website": "unbounce.com"
        },
        "Underscore.js": {
            "cats": [
                12
            ],
            "icon": "Underscore.js.png",
            "script": "underscore.*\\.js",
            "website": "underscorejs.org"
        },
        "UserRules": {
            "cats": [
                13
            ],
            "env": "^_usrp$",
            "icon": "UserRules.png",
            "website": "www.userrules.com"
        },
        "UserVoice": {
            "cats": [
                13
            ],
            "env": "^UserVoice$",
            "icon": "UserVoice.png",
            "website": "uservoice.com"
        },
        "Ushahidi": {
            "cats": [
                1,
                35
            ],
            "env": "^Ushahidi$",
            "headers": {
                "Set-Cookie": "^ushahidi="
            },
            "icon": "Ushahidi.png",
            "implies": [
                "PHP",
                "MySQL",
                "OpenLayers"
            ],
            "script": "/js/ushahidi\\.js$",
            "website": "www.ushahidi.com"
        },
        "VIVVO": {
            "cats": [
                1
            ],
            "env": "^vivvo",
            "headers": {
                "Set-Cookie": "VivvoSessionId"
            },
            "icon": "VIVVO.png",
            "website": "vivvo.net"
        },
        "VP-ASP": {
            "cats": [
                6
            ],
            "html": "<a[^>]+>Powered By VP-ASP Shopping Cart</a>",
            "icon": "VP-ASP.png",
            "implies": "Microsoft ASP.NET",
            "script": "vs350\\.js",
            "website": "www.vpasp.com"
        },
        "VTEX Enterprise": {
            "cats": [
                6
            ],
            "headers": {
                "powered": "vtex"
            },
            "icon": "VTEX Enterprise.png",
            "website": "vtex.com"
        },
        "VTEX Integrated Store": {
            "cats": [
                6
            ],
            "headers": {
                "X-Powered-By": "vtex-integrated-store"
            },
            "icon": "VTEX Integrated Store.png",
            "website": "lojaintegrada.com.br"
        },
        "Vanilla": {
            "cats": [
                2
            ],
            "headers": {
                "X-Powered-By": "Vanilla"
            },
            "html": "<body id=\"(?:DiscussionsPage|vanilla)",
            "icon": "Vanilla.png",
            "implies": "PHP",
            "website": "vanillaforums.org"
        },
        "Varnish": {
            "cats": [
                23
            ],
            "headers": {
                "Via": ".*Varnish",
                "X-Varnish": "",
                "X-Varnish-Action": "",
                "X-Varnish-Age": "",
                "X-Varnish-Cache": "",
                "X-Varnish-Hostname": ""
            },
            "icon": "Varnish.svg",
            "website": "www.varnish-cache.org"
        },
        "Venda": {
            "cats": [
                6
            ],
            "headers": {
                "X-venda-hitid": ""
            },
            "icon": "Venda.png",
            "website": "venda.com"
        },
        "Veoxa": {
            "cats": [
                36
            ],
            "env": "^(?:Veoxa_|VuVeoxaContent)",
            "html": "<img [^>]*src=\"[^\"]+tracking\\.veoxa\\.com",
            "icon": "Veoxa.png",
            "script": "tracking\\.veoxa\\.com",
            "website": "veoxa.com"
        },
        "VideoJS": {
            "cats": [
                14
            ],
            "env": "^VideoJS$",
            "html": "<div[^>]+class=\"video-js+\">",
            "icon": "VideoJS.png",
            "script": "zencdn\\.net/c/video\\.js",
            "website": "videojs.com"
        },
        "VigLink": {
            "cats": [
                36
            ],
            "env": "^(?:vglnk(?:$|_)|vl_(?:cB|disable)$)",
            "icon": "VigLink.png",
            "script": "(?:^[^/]*//[^/]*viglink\\.com/api/|vglnk\\.js)",
            "website": "viglink.com"
        },
        "Vignette": {
            "cats": [
                1
            ],
            "html": "<[^>]+=\"vgn-?ext",
            "icon": "Vignette.png",
            "website": "www.vignette.com"
        },
        "Vimeo": {
            "cats": [
                14
            ],
            "html": "(?:<(?:param|embed)[^>]+vimeo\\.com/moogaloop|<iframe[^>]player\\.vimeo\\.com)",
            "icon": "Vimeo.png",
            "website": "vimeo.com"
        },
        "Virata EmWeb": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Virata-EmWeb(?:/(R?[\\d._]+))?\\;version:\\1"
            },
            "icon": "default.png",
            "implies": [
                "HP"
            ],
            "website": "???"
        },
        "VirtueMart": {
            "cats": [
                6
            ],
            "html": "<div id=\"vmMainPage",
            "icon": "VirtueMart.png",
            "implies": "Joomla",
            "website": "virtuemart.net"
        },
        "Visual WebGUI": {
            "cats": [
                18
            ],
            "env": "^VWGEventArgs$",
            "icon": "Visual WebGUI.png",
            "implies": "Microsoft ASP.NET",
            "meta": {
                "generator": "^Visual WebGUI"
            },
            "script": "\\.js\\.wgx$",
            "url": "\\.wgx$",
            "website": "www.gizmox.com/products/visual-web-gui/"
        },
        "VisualPath": {
            "cats": [
                10
            ],
            "icon": "VisualPath.png",
            "script": "visualpath[^/]*\\.trackset\\.it/[^/]+/track/include\\.js",
            "website": "www.trackset.com/web-analytics-software/visualpath"
        },
        "Volusion": {
            "cats": [
                6
            ],
            "env": "^volusion$",
            "html": "<link [^>]*href=\"[^\"]*/vspfiles/",
            "icon": "Volusion.png",
            "script": "/volusion\\.js(?:\\?([\\d.]*))?\\;version:\\1",
            "website": "volusion.com"
        },
        "Vox": {
            "cats": [
                11
            ],
            "icon": "Vox.png",
            "url": "\\.vox\\.com",
            "website": "www.vox.com"
        },
        "Vue.js": {
            "cats": [
                12
            ],
            "env": "^Vue$",
            "icon": "Vue.js.png",
            "script": [
                "vue(?:\\-|\\.)([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
                "/([\\d.]+)/vue(?:\\.min)?\\.js\\;version:\\1",
                "vue.*\\.js"
            ],
            "website": "vuejs.org"
        },
        "W3 Total Cache": {
            "cats": [
                23
            ],
            "headers": {
                "X-Powered-By": "W3 Total Cache(?:/([\\d.]+))?\\;version:\\1"
            },
            "html": "<!--[^>]+W3 Total Cache",
            "icon": "W3 Total Cache.png",
            "implies": "WordPress",
            "website": "www.w3-edge.com/wordpress-plugins/w3-total-cache"
        },
        "W3Counter": {
            "cats": [
                10
            ],
            "icon": "W3Counter.png",
            "script": "w3counter\\.com/tracker\\.js",
            "website": "www.w3counter.com"
        },
        "WHMCS": {
            "cats": [
                6
            ],
            "headers": {
                "Set-Cookie": "^WHMCS.*"
            },
            "icon": "WHMCS.png",
            "website": "www.whmcs.com"
        },
        "WP Rocket": {
            "cats": [
                23
            ],
            "headers": {
                "X-Powered-By": "WP Rocket(?:/([\\d.]+))?\\;version:\\1"
            },
            "html": "<!--[^>]+WP Rocket",
            "icon": "WP Rocket.png",
            "implies": "WordPress",
            "website": "wp-rocket.me"
        },
        "Warp": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "^Warp/(\\d+(?:\\.\\d+)+)?$\\;version:\\1"
            },
            "icon": "Warp.png",
            "implies": "Haskell",
            "website": "www.stackage.org/package/warp"
        },
        "Web Optimizer": {
            "cats": [
                10
            ],
            "html": "<title [^>]*lang=\"wo\">",
            "icon": "Web Optimizer.png",
            "website": "www.web-optimizer.us"
        },
        "Web2py": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "web2py"
            },
            "icon": "Web2py.png",
            "implies": [
                "Python",
                "jQuery"
            ],
            "meta": {
                "generator": "^Web2py"
            },
            "script": "web2py\\.js",
            "website": "web2py.com"
        },
        "WebGUI": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "^wgSession="
            },
            "icon": "WebGUI.png",
            "implies": "Perl",
            "meta": {
                "generator": "^WebGUI ([\\d.]+)\\;version:\\1"
            },
            "website": "www.webgui.org"
        },
        "WebPublisher": {
            "cats": [
                1
            ],
            "icon": "WebPublisher.png",
            "meta": {
                "generator": "WEB\\|Publisher"
            },
            "website": "scannet.dk"
        },
        "Webix": {
            "cats": [
                12
            ],
            "env": "^webix$",
            "icon": "Webix.png",
            "script": "\bwebix\\.js",
            "website": "webix.com"
        },
        "Webs": {
            "cats": [
                1
            ],
            "headers": {
                "Server": "Webs\\.com/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "Webs.png",
            "website": "webs.com"
        },
        "WebsPlanet": {
            "cats": [
                1
            ],
            "icon": "WebsPlanet.png",
            "meta": {
                "generator": "WebsPlanet"
            },
            "website": "websplanet.com"
        },
        "Websale": {
            "cats": [
                6
            ],
            "icon": "Websale.png",
            "url": "/websale7/",
            "website": "websale.de"
        },
        "WebsiteBaker": {
            "cats": [
                1
            ],
            "icon": "WebsiteBaker.png",
            "implies": [
                "PHP",
                "MySQL"
            ],
            "meta": {
                "generator": "WebsiteBaker"
            },
            "website": "websitebaker2.org/en/home.php"
        },
        "Webtrekk": {
            "cats": [
                10
            ],
            "env": "^webtrekk",
            "icon": "Webtrekk.png",
            "website": "www.webtrekk.com"
        },
        "Webtrends": {
            "cats": [
                10
            ],
            "env": "^(?:WTOptimize|WebTrends)",
            "html": "<img[^>]+id=\"DCSIMG\"[^>]+webtrends",
            "icon": "Webtrends.png",
            "website": "worldwide.webtrends.com"
        },
        "Weebly": {
            "cats": [
                1
            ],
            "icon": "Weebly.png",
            "script": "cdn\\d+\\.editmysite\\.com",
            "website": "www.weebly.com"
        },
        "Wikispaces": {
            "cats": [
                8
            ],
            "html": [
                "<script[^>]*>[^<]*session_url:\\s*'https://session\\.wikispaces\\.com/",
                "<\\w+[^>]*\\s+class=\"[^\"]*WikispacesContent\\s+WikispacesBs3[^\"]*\""
            ],
            "icon": "Wikispaces.png",
            "website": "www.wikispaces.com"
        },
        "WikkaWiki": {
            "cats": [
                8
            ],
            "html": "Powered by <a href=\"[^>]+WikkaWiki",
            "icon": "WikkaWiki.png",
            "meta": {
                "generator": "WikkaWiki"
            },
            "website": "wikkawiki.org"
        },
        "Windows CE": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "\bWinCE\b"
            },
            "icon": "Microsoft.svg",
            "website": "microsoft.com"
        },
        "Windows Server": {
            "cats": [
                28
            ],
            "headers": {
                "Server": "Win32|Win64"
            },
            "icon": "Microsoft.svg",
            "website": "microsoft.com/windowsserver"
        },
        "Wink": {
            "cats": [
                26,
                12
            ],
            "env": "^wink$",
            "icon": "Wink.png",
            "script": "(?:_base/js/base|wink).*\\.js",
            "website": "winktoolkit.org"
        },
        "Winstone Servlet Container": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Winstone Servlet (?:Container|Engine) v?([\\d.]+)?\\;version:\\1",
                "X-Powered-By": "Winstone(?:.([\\d.]+))?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "winstone.sourceforge.net"
        },
        "Wix": {
            "cats": [
                1
            ],
            "env": "^wix(?:Events|Data|Errors)",
            "headers": {
                "Set-Cookie": "Domain=\\.wix\\.com",
                "X-Wix-Dispatcher-Cache-Hit": ""
            },
            "icon": "Wix.png",
            "script": "static\\.wixstatic\\.com",
            "website": "wix.com"
        },
        "Wolf CMS": {
            "cats": [
                1
            ],
            "html": "(?:<a href=\"[^>]+wolfcms\\.org[^>]+>Wolf CMS(?:</a>)? inside|Thank you for using <a[^>]+>Wolf CMS)",
            "icon": "Wolf CMS.png",
            "website": "www.wolfcms.org"
        },
        "Woltlab Community Framework": {
            "cats": [
                18
            ],
            "html": "var WCF_PATH[^>]+",
            "icon": "Woltlab Community Framework.png",
            "implies": "PHP",
            "script": "WCF\\..*\\.js",
            "website": "www.woltlab.com"
        },
        "WooCommerce": {
            "cats": [
                6
            ],
            "env": "woocommerce",
            "html": "<!-- WooCommerce",
            "icon": "WooCommerce.png",
            "implies": [
                "WordPress",
                "PHP"
            ],
            "meta": {
                "generator": "WooCommerce ([\\d.]+)\\;version:\\1"
            },
            "script": "woocommerce",
            "website": "www.woothemes.com/woocommerce"
        },
        "Woopra": {
            "cats": [
                10
            ],
            "icon": "Woopra.png",
            "script": "static\\.woopra\\.com",
            "website": "www.woopra.com"
        },
        "WordPress": {
            "cats": [
                1,
                11
            ],
            "env": "^wp_username$",
            "html": [
                "<link rel=[\"']stylesheet[\"'] [^>]+wp-(?:content|includes)",
                "<link[^>]+s\\d+\\.wp\\.com"
            ],
            "icon": "WordPress.svg",
            "implies": "PHP",
            "meta": {
                "generator": "WordPress( [\\d.]+)?\\;version:\\1"
            },
            "script": "/wp-includes/",
            "website": "wordpress.org"
        },
        "WordPress Super Cache": {
            "cats": [
                23
            ],
            "html": "<!--[^>]+WP-Super-Cache",
            "icon": "default.png",
            "implies": "WordPress",
            "website": "z9.io/wp-super-cache/"
        },
        "Wowza Media Server": {
            "cats": [
                38
            ],
            "html": "<title>Wowza Media Server \\d+ ((?:\\w+ Edition )?\\d+\\.[\\d\\.]+(?: build\\d+)?)?\\;version:\\1",
            "icon": "Wowza Media Server.png",
            "website": "www.wowza.com"
        },
        "X-Cart": {
            "cats": [
                6
            ],
            "env": "^(?:xcart_web_dir|xliteConfig)$",
            "headers": {
                "Set-Cookie": "xid=[a-z\\d]{32}(?:;|$)"
            },
            "html": [
                "Powered by X-Cart(?: (\\d+))? <a[^>]+href=\"http://www\\.x-cart\\.com/\"[^>]*>\\;version:\\1",
                "<a[^>]+href=\"[^\"]*(?:\\?|&)xcart_form_id=[a-z\\d]{32}(?:&|$)"
            ],
            "icon": "X-Cart.png",
            "implies": "PHP",
            "meta": {
                "generator": "X-Cart(?: (\\d+))?\\;version:\\1"
            },
            "script": "/skin/common_files/modules/Product_Options/func\\.js",
            "website": "x-cart.com"
        },
        "XAMPP": {
            "cats": [
                22
            ],
            "html": "<title>XAMPP(?: Version ([\\d\\.]+))?</title>\\;version:\\1",
            "icon": "XAMPP.png",
            "implies": [
                "Apache",
                "MySQL",
                "PHP",
                "Perl"
            ],
            "meta": {
                "author": "Kai Oswald Seidler"
            },
            "website": "www.apachefriends.org/en/xampp.html"
        },
        "XMB": {
            "cats": [
                2
            ],
            "html": "<!-- Powered by XMB",
            "icon": "XMB.png",
            "website": "www.xmbforum.com"
        },
        "XOOPS": {
            "cats": [
                1
            ],
            "env": "^xoops",
            "icon": "XOOPS.png",
            "implies": "PHP",
            "meta": {
                "generator": "XOOPS"
            },
            "website": "xoops.org"
        },
        "XRegExp": {
            "cats": [
                12
            ],
            "env": "^XRegExp$",
            "icon": "XRegExp.png",
            "script": [
                "xregexp(?:\\-|\\.)([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
                "/([\\d.]+)/xregexp(?:\\.min)?\\.js\\;version:\\1",
                "xregexp.*\\.js"
            ],
            "website": "xregexp.com"
        },
        "Xajax": {
            "cats": [
                12
            ],
            "icon": "Xajax.png",
            "script": "xajax_core.*\\.js",
            "website": "xajax-project.org"
        },
        "Xanario": {
            "cats": [
                6
            ],
            "icon": "Xanario.png",
            "meta": {
                "generator": "xanario shopsoftware"
            },
            "website": "xanario.de"
        },
        "XenForo": {
            "cats": [
                2
            ],
            "html": "(?:jQuery\\.extend\\(true, XenForo|Forum software by XenForo&trade;|<!--XF:branding|<html[^>]+id=\"XenForo\")",
            "icon": "XenForo.png",
            "website": "xenforo.com"
        },
        "Xitami": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Xitami(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Xitami.png",
            "website": "xitami.com"
        },
        "Xonic": {
            "cats": [
                6
            ],
            "html": [
                "Powered by <a href=\"http://www.xonic-solutions.de/index.php\" target=\"_blank\">xonic-solutions Shopsoftware</a>"
            ],
            "icon": "xonic.png",
            "meta": {
                "keywords": "xonic-solutions"
            },
            "script": "core/jslib/jquery\\.xonic\\.js\\.php",
            "website": "www.xonic-solutions.de"
        },
        "XpressEngine": {
            "cats": [
                1
            ],
            "icon": "XpressEngine.png",
            "meta": {
                "generator": "XpressEngine"
            },
            "website": "www.xpressengine.com/"
        },
        "YUI": {
            "cats": [
                12
            ],
            "env": "^YAHOO$",
            "icon": "YUI.png",
            "script": "(?:/yui/|yui\\.yahooapis\\.com)",
            "website": "yuilibrary.com"
        },
        "YUI Doc": {
            "cats": [
                4
            ],
            "html": "(?:<html[^>]* yuilibrary\\.com/rdf/[\\d.]+/yui\\.rdf|<body[^>]+class=\"yui3-skin-sam)",
            "icon": "YUI Doc.png",
            "website": "developer.yahoo.com/yui/yuidoc"
        },
        "YaBB": {
            "cats": [
                2
            ],
            "html": "Powered by <a href=\"[^>]+yabbforum",
            "icon": "YaBB.png",
            "website": "www.yabbforum.com"
        },
        "Yahoo Advertising": {
            "cats": [
                36
            ],
            "env": "^adxinserthtml$",
            "html": [
                "<iframe[^>]+adserver\\.yahoo\\.com",
                "<img[^>]+clicks\\.beap\\.bc\\.yahoo\\.com"
            ],
            "icon": "Yahoo Advertising.png",
            "script": "adinterax\\.com",
            "website": "advertising.yahoo.com"
        },
        "Yahoo! Ecommerce": {
            "cats": [
                6
            ],
            "env": "^YStore$",
            "headers": {
                "X-XRDS-Location": "/ystore/"
            },
            "html": "<link[^>]+store\\.yahoo\\.net",
            "icon": "Yahoo! Ecommerce.png",
            "website": "smallbusiness.yahoo.com/ecommerce"
        },
        "Yahoo! Web Analytics": {
            "cats": [
                10
            ],
            "env": "^YWA$",
            "icon": "Yahoo! Web Analytics.png",
            "script": "d\\.yimg\\.com/mi/ywa\\.js",
            "website": "web.analytics.yahoo.com"
        },
        "Yandex.Direct": {
            "cats": [
                36
            ],
            "env": [
                "^yandex_partner_id$",
                "^yandex_ad_format$",
                "^yandex_direct_"
            ],
            "html": "<yatag class=\"ya-partner__ads\">",
            "icon": "Yandex.Direct.png",
            "script": "https?://an\\.yandex\\.ru/",
            "website": "partner.yandex.com"
        },
        "Yandex.Metrika": {
            "cats": [
                10
            ],
            "env": "^yandex_metrika",
            "icon": "Yandex.Metrika.png",
            "script": "mc\\.yandex\\.ru\\/metrika\\/watch\\.js",
            "website": "metrika.yandex.com"
        },
        "Yaws": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "Yaws(?: ([\\d.]+))?\\;version:\\1"
            },
            "icon": "Yaws.png",
            "implies": [
                "Erlang"
            ],
            "website": "yaws.hyber.org"
        },
        "Yieldlab": {
            "cats": [
                36
            ],
            "icon": "Yieldlab.png",
            "script": "^https?://(?:[^/]+\\.)?yieldlab\\.net/",
            "website": "yieldlab.de"
        },
        "Yii": {
            "cats": [
                18
            ],
            "html": [
                "Powered by <a href=\"http://www.yiiframework.com/\" rel=\"external\">Yii Framework</a>"
            ],
            "icon": "Yii.png",
            "implies": [
                "PHP"
            ],
            "website": "yiiframework.com"
        },
        "Yoast SEO": {
            "cats": [
                32
            ],
            "html": [
                "<!-- This site is optimized with the Yoast"
            ],
            "icon": "Yoast SEO.png",
            "website": "yoast.com"
        },
        "YouTube": {
            "cats": [
                14
            ],
            "html": "<(?:param|embed|iframe)[^>]+youtube(?:-nocookie)?\\.com/(?:v|embed)",
            "icon": "YouTube.png",
            "website": "www.youtube.com"
        },
        "ZK": {
            "cats": [
                18
            ],
            "html": "<!-- ZK [\\.\\d\\s]+-->",
            "icon": "ZK.png",
            "implies": "Java",
            "script": "zkau/",
            "website": "zkoss.org"
        },
        "ZURB Foundation": {
            "cats": [
                18
            ],
            "html": [
                "<link[^>]+foundation[^>\"]+css",
                "<div [^>]*class=\"[^\"]*(?:small|medium|large)-\\d{1,2} columns"
            ],
            "icon": "ZURB Foundation.png",
            "website": "foundation.zurb.com"
        },
        "Zabbix": {
            "cats": [
                19
            ],
            "env": "^zbxCallPostScripts$",
            "html": "<body[^>]+zbxCallPostScripts",
            "icon": "Zabbix.png",
            "meta": {
                "Author": "ZABBIX SIA"
            },
            "url": "\\/zabbix\\/",
            "website": "zabbix.com"
        },
        "Zanox": {
            "cats": [
                36
            ],
            "env": "^zanox$",
            "html": "<img [^>]*src=\"[^\"]+ad\\.zanox\\.com",
            "icon": "Zanox.png",
            "script": "zanox\\.com/scripts/zanox\\.js$",
            "website": "zanox.com"
        },
        "Zen Cart": {
            "cats": [
                6
            ],
            "icon": "Zen Cart.png",
            "meta": {
                "generator": "Zen Cart"
            },
            "website": "www.zen-cart.com"
        },
        "Zend": {
            "cats": [
                22
            ],
            "headers": {
                "Set-Cookie": "ZENDSERVERSESSID",
                "X-Powered-By": "Zend"
            },
            "icon": "Zend.png",
            "website": "zend.com"
        },
        "Zepto": {
            "cats": [
                12
            ],
            "env": "^Zepto$",
            "icon": "Zepto.png",
            "script": "zepto.*\\.js",
            "website": "zeptojs.com"
        },
        "Zeuscart": {
            "cats": [
                6
            ],
            "html": "<form name=\"product\" method=\"post\" action=\"[^\"]+\\?do=addtocart&prodid=\\d+\"(?!<\\/form>.)+<input type=\"hidden\" name=\"addtocart\" value=\"\\d+\">",
            "icon": "Zeuscart.png",
            "implies": "PHP",
            "url": "\\?do=prodetail&action=show&prodid=\\d+",
            "website": "zeuscart.com"
        },
        "Zinnia": {
            "cats": [
                11
            ],
            "icon": "Zinnia.png",
            "implies": "Django",
            "meta": {
                "generator": "Zinnia"
            },
            "website": "django-blog-zinnia.com"
        },
        "Zope": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "^Zope/"
            },
            "icon": "Zope.png",
            "website": "zope.org"
        },
        "a-blog cms": {
            "cats": [
                1
            ],
            "icon": "a-blog cms.png",
            "implies": "PHP",
            "meta": {
                "generator": "a-blog cms"
            },
            "website": "www.a-blogcms.jp"
        },
        "actionhero.js": {
            "cats": [
                1,
                18,
                22
            ],
            "env": "^actionheroClient$",
            "headers": {
                "X-Powered-By": "actionhero API"
            },
            "icon": "actionhero.js.png",
            "implies": "Node.js",
            "script": "actionheroClient\\.js",
            "website": "www.actionherojs.com"
        },
        "amCharts": {
            "cats": [
                25
            ],
            "env": "^AmCharts$",
            "icon": "amCharts.png",
            "script": "amcharts.*\\.js",
            "website": "amcharts.com"
        },
        "basket.js": {
            "cats": [
                12
            ],
            "env": "^basket$",
            "icon": "basket.js.png",
            "script": "basket.*\\.js",
            "website": "addyosmani.github.io/basket.js/"
        },
        "cPanel": {
            "cats": [
                9
            ],
            "headers": {
                "Server": "cpsrvd/([\\d.]+)\\;version:\\1"
            },
            "html": "<!-- cPanel",
            "icon": "cPanel.png",
            "website": "www.cpanel.net"
        },
        "cgit": {
            "cats": [
                19
            ],
            "html": "<[^>]+id='cgit'",
            "icon": "cgit.png",
            "implies": "Perl",
            "website": "git.zx2c4.com/cgit"
        },
        "comScore": {
            "cats": [
                10
            ],
            "env": "^_?COMSCORE$",
            "html": "<iframe[^>]* (?:id=\"comscore\"|scr=[^>]+comscore)|\\.scorecardresearch\\.com/beacon\\.js|COMSCORE\\.beacon",
            "icon": "comScore.png",
            "script": "\\.scorecardresearch\\.com/beacon\\.js|COMSCORE\\.beacon",
            "website": "comscore.com"
        },
        "debut": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "debut\\/?([\\d\\.]+)?\\;version:\\1"
            },
            "icon": "debut.png",
            "implies": "Brother",
            "website": "www.brother.com"
        },
        "dwhttpd": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "dwhttpd\\/?([\\d\\.a-z]+)?\\;version:\\1"
            },
            "icon": "default.png",
            "website": "???"
        },
        "e107": {
            "cats": [
                1
            ],
            "headers": {
                "Set-Cookie": "e107_tz[^;]+=",
                "X-Powered-By": "e107"
            },
            "icon": "e107.png",
            "implies": "PHP",
            "script": "[^a-z\\d]e107\\.js",
            "website": "e107.org"
        },
        "eDevice SmartStack": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "eDevice SmartStack(?: ?/?([\\d.]+))?\\;version:\\1"
            },
            "icon": "eDevice SmartStack.png",
            "website": "edevice.com"
        },
        "eHTTP": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "\beHTTP(?: v?([\\d\\.]+))?\\;version:\\1"
            },
            "icon": "default.png",
            "implies": "HP ProCurve",
            "website": "???"
        },
        "eSyndiCat": {
            "cats": [
                1
            ],
            "env": "^esyndicat$",
            "headers": {
                "X-Drectory-Script": "^eSyndiCat"
            },
            "icon": "eSyndiCat.png",
            "implies": "PHP",
            "meta": {
                "generator": "^eSyndiCat "
            },
            "website": "esyndicat.com"
        },
        "eZ Publish": {
            "cats": [
                1,
                6
            ],
            "headers": {
                "X-Powered-By": "^eZ Publish"
            },
            "icon": "eZ Publish.png",
            "implies": "PHP",
            "meta": {
                "generator": "eZ Publish"
            },
            "website": "ez.no"
        },
        "git": {
            "cats": [
                47
            ],
            "icon": "git.png",
            "meta": {
                "generator": "\bgit/([\\d.]+\\d)\\;version:\\1"
            },
            "website": "git-scm.com"
        },
        "gitweb": {
            "cats": [
                47
            ],
            "html": "<!-- git web interface version",
            "icon": "gitweb.png",
            "implies": [
                "Perl",
                "git"
            ],
            "meta": {
                "generator": "gitweb(?:/([\\d.]+\\d))?\\;version:\\1"
            },
            "website": "git-scm.com"
        },
        "gunicorn": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "gunicorn(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "gunicorn.png",
            "implies": [
                "Python"
            ],
            "website": "gunicorn.org"
        },
        "hapi.js": {
            "cats": [
                18,
                22
            ],
            "headers": {
                "Set-Cookie": "Fe26\\.2\\*\\*"
            },
            "icon": "hapi.js.png",
            "implies": "Node.js",
            "website": "hapijs.com"
        },
        "iCongo": {
            "cats": [
                6
            ],
            "icon": "iCongo.png",
            "implies": "Adobe ColdFusion",
            "meta": {
                "iCongo": ""
            },
            "website": "hybris.com/icongo"
        },
        "iWeb": {
            "cats": [
                20
            ],
            "icon": "iWeb.png",
            "meta": {
                "generator": "^iWeb( [\\d.]+)?\\;version:\\1"
            },
            "website": "apple.com/ilife/iweb"
        },
        "io4 CMS": {
            "cats": [
                1
            ],
            "icon": "io4 CMS.png",
            "meta": {
                "generator": "GO[ |]+CMS Enterprise"
            },
            "website": "notenbomer.nl/Producten/Content_management/io4_|_cms"
        },
        "jQTouch": {
            "cats": [
                26
            ],
            "env": "^jQT$",
            "icon": "jQTouch.png",
            "script": "jqtouch.*\\.js",
            "website": "jqtouch.com"
        },
        "jQuery": {
            "cats": [
                12
            ],
            "env": "^jQuery$",
            "icon": "jQuery.svg",
            "script": [
                "jquery(?:\\-|\\.)([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
                "/([\\d.]+)/jquery(?:\\.min)?\\.js\\;version:\\1",
                "jquery.*\\.js"
            ],
            "website": "jquery.com"
        },
        "jQuery Mobile": {
            "cats": [
                26
            ],
            "icon": "jQuery Mobile.svg",
            "implies": "jQuery",
            "script": "jquery\\.mobile(?:-([\\d.]+rc\\d))?.*\\.js(?:\\?ver=([\\d.]+))?\\;version:\\1?\\1:\\2",
            "website": "jquerymobile.com"
        },
        "jQuery Sparklines": {
            "cats": [
                25
            ],
            "icon": "default.png",
            "implies": "jQuery",
            "script": "jquery\\.sparkline.*\\.js",
            "website": "omnipotent.net/jquery.sparkline/"
        },
        "jQuery UI": {
            "cats": [
                12
            ],
            "icon": "jQuery UI.svg",
            "implies": "jQuery",
            "script": [
                "jquery-ui(?:-|\\.)([\\d.]*\\d)[^/]*\\.js\\;version:\\1",
                "([\\d.]+)/jquery-ui(?:\\.min)?\\.js\\;version:\\1",
                "jquery-ui.*\\.js"
            ],
            "website": "jqueryui.com"
        },
        "jqPlot": {
            "cats": [
                25
            ],
            "icon": "jqPlot.png",
            "implies": "jQuery",
            "script": "jqplot.*\\.js",
            "website": "www.jqplot.com"
        },
        "libwww-perl-daemon": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "libwww-perl-daemon(?:/([\\d\\.]+))?\\;version:\\1"
            },
            "icon": "libwww-perl-daemon.png",
            "implies": "Perl",
            "website": "metacpan.org/pod/HTTP::Daemon"
        },
        "lighttpd": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "lighttpd(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "lighttpd.png",
            "website": "www.lighttpd.net"
        },
        "math.js": {
            "cats": [
                12
            ],
            "env": "^mathjs$",
            "icon": "math.js.png",
            "script": "math(?:\\.min)?\\.js",
            "website": "mathjs.org"
        },
        "mini_httpd": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "mini_httpd(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "mini_httpd.png",
            "website": "acme.com/software/mini_httpd"
        },
        "mod_auth_pam": {
            "cats": [
                33
            ],
            "headers": {
                "Server": "mod_auth_pam(?:/([\\d\\.]+))?\\;version:\\1"
            },
            "icon": "Apache.svg",
            "implies": "Apache",
            "website": "pam.sourceforge.net/mod_auth_pam"
        },
        "mod_dav": {
            "cats": [
                33
            ],
            "headers": {
                "Server": "\b(?:mod_)?DAV\b(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Apache.svg",
            "implies": "Apache",
            "website": "webdav.org/mod_dav"
        },
        "mod_fastcgi": {
            "cats": [
                33
            ],
            "headers": {
                "Server": "mod_fastcgi(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "Apache.svg",
            "implies": "Apache",
            "website": "www.fastcgi.com/mod_fastcgi/docs/mod_fastcgi.html"
        },
        "mod_jk": {
            "cats": [
                33
            ],
            "headers": {
                "Server": "mod_jk(?:/([\\d\\.]+))?\\;version:\\1"
            },
            "icon": "Apache.svg",
            "implies": [
                "Apache Tomcat",
                "Apache"
            ],
            "website": "tomcat.apache.org/tomcat-3.3-doc/mod_jk-howto.html"
        },
        "mod_perl": {
            "cats": [
                33
            ],
            "headers": {
                "Server": "mod_perl(?:/([\\d\\.]+))?\\;version:\\1"
            },
            "icon": "mod_perl.png",
            "implies": [
                "Perl",
                "Apache"
            ],
            "website": "perl.apache.org"
        },
        "mod_python": {
            "cats": [
                33
            ],
            "headers": {
                "Server": "mod_python(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "mod_python.png",
            "implies": [
                "Python",
                "Apache"
            ],
            "website": "www.modpython.org"
        },
        "mod_rack": {
            "cats": [
                33
            ],
            "headers": {
                "Server": "mod_rack(?:/([\\d.]+))?\\;version:\\1",
                "X-Powered-By": "mod_rack(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "mod_rack.png",
            "implies": [
                "Ruby on Rails",
                "Apache"
            ],
            "website": "phusionpassenger.com"
        },
        "mod_rails": {
            "cats": [
                33
            ],
            "headers": {
                "Server": "mod_rails(?:/([\\d.]+))?\\;version:\\1",
                "X-Powered-By": "mod_rails(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "mod_rails.png",
            "implies": [
                "Ruby on Rails",
                "Apache"
            ],
            "website": "phusionpassenger.com"
        },
        "mod_ssl": {
            "cats": [
                33
            ],
            "headers": {
                "Server": "mod_ssl(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "mod_ssl.png",
            "implies": "Apache",
            "website": "modssl.org"
        },
        "mod_wsgi": {
            "cats": [
                33
            ],
            "headers": {
                "Server": "mod_wsgi(?:/([\\d.]+))?\\;version:\\1",
                "X-Powered-By": "mod_wsgi(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "mod_wsgi.png",
            "implies": [
                "Python",
                "Apache"
            ],
            "website": "code.google.com/p/modwsgi"
        },
        "nopCommerce": {
            "cats": [
                6
            ],
            "html": "(?:<!--Powered by nopCommerce|Powered by: <a[^>]+nopcommerce)",
            "icon": "nopCommerce.png",
            "website": "www.nopcommerce.com"
        },
        "openEngine": {
            "cats": [
                1
            ],
            "icon": "openEngine.png",
            "meta": {
                "openEngine": ""
            },
            "website": "openengine.de/html/pages/de/"
        },
        "osCSS": {
            "cats": [
                6
            ],
            "html": "<body onload=\"window\\.defaultStatus='oscss templates';\"",
            "icon": "osCSS.png",
            "website": "www.oscss.org"
        },
        "osCommerce": {
            "cats": [
                6
            ],
            "headers": {
                "Set-Cookie": "osCsid="
            },
            "html": "(?:<a[^>]*(?:\\?|&)osCsid|Powered by (?:<[^>]+>)?osCommerce</a>|<[^>]+class=\"[^>]*infoBoxHeading)",
            "icon": "osCommerce.png",
            "website": "www.oscommerce.com"
        },
        "osTicket": {
            "cats": [
                13
            ],
            "headers": {
                "Set-Cookie": "OSTSESSID"
            },
            "icon": "osTicket.png",
            "implies": [
                "PHP",
                "MySQL"
            ],
            "website": "osticket.com"
        },
        "ownCloud": {
            "cats": [
                19
            ],
            "html": "<a href=\"https://owncloud.com\" target=\"_blank\">ownCloud Inc.</a><br/>Your Cloud, Your Data, Your Way!",
            "icon": "ownCloud.png",
            "meta": {
                "apple-itunes-app": "app-id=543672169"
            },
            "website": "owncloud.org"
        },
        "papaya CMS": {
            "cats": [
                1
            ],
            "html": "<link[^>]*/papaya-themes/",
            "icon": "papaya CMS.png",
            "website": "papaya-cms.com"
        },
        "phpAlbum": {
            "cats": [
                7
            ],
            "html": "<!--phpalbum ([.\\d\\s]+)-->\\;version:\\1",
            "icon": "phpAlbum.png",
            "implies": "PHP",
            "website": "phpalbum.net"
        },
        "phpBB": {
            "cats": [
                2
            ],
            "env": "^(?:style_cookie_settings|phpbb_)",
            "headers": {
                "Set-Cookie": "^phpbb"
            },
            "html": "(?:Powered by <a[^>]+phpbb|<a[^>]+phpbb[^>]+class=\\.copyright|\tphpBB style name|<[^>]+styles/(?:sub|pro)silver/theme|<img[^>]+i_icon_mini|<table class=\"forumline)",
            "icon": "phpBB.png",
            "implies": "PHP",
            "meta": {
                "copyright": "phpBB Group"
            },
            "website": "phpbb.com"
        },
        "phpCMS": {
            "cats": [
                1
            ],
            "env": "^phpcms",
            "icon": "phpCMS.png",
            "implies": "PHP",
            "website": "phpcms.de"
        },
        "phpDocumentor": {
            "cats": [
                4
            ],
            "html": "<!-- Generated by phpDocumentor",
            "icon": "phpDocumentor.png",
            "implies": "PHP",
            "website": "www.phpdoc.org"
        },
        "phpMyAdmin": {
            "cats": [
                3
            ],
            "env": "^pma_absolute_uri$",
            "html": "(?: \\| phpMyAdmin ([\\d.]+)<\\/title>|PMA_sendHeaderLocation\\(|<link [^>]*href=\"[^\"]*phpmyadmin\\.css\\.php)\\;version:\\1",
            "icon": "phpMyAdmin.png",
            "implies": [
                "PHP",
                "MySQL"
            ],
            "website": "www.phpmyadmin.net"
        },
        "phpPgAdmin": {
            "cats": [
                3
            ],
            "html": "(?:<title>phpPgAdmin</title>|<span class=\"appname\">phpPgAdmin)",
            "icon": "phpPgAdmin.png",
            "implies": "PHP",
            "website": "phppgadmin.sourceforge.net"
        },
        "phpSQLiteCMS": {
            "cats": [
                1
            ],
            "icon": "phpSQLiteCMS.png",
            "implies": [
                "PHP",
                "SQLite"
            ],
            "meta": {
                "generator": "^phpSQLiteCMS(?: (.+))?$\\;version:\\1"
            },
            "website": "phpsqlitecms.net"
        },
        "phpwind": {
            "cats": [
                1,
                2
            ],
            "html": "Powered by <a href=\"[^\"]+phpwind\\.net",
            "icon": "phpwind.png",
            "implies": "PHP",
            "meta": {
                "generator": "^phpwind"
            },
            "website": "www.phpwind.net"
        },
        "prettyPhoto": {
            "cats": [
                7,
                12
            ],
            "env": "pp_(?:alreadyInitialized|descriptions|images|titles)",
            "html": "(?:<link [^>]*href=\"[^\"]*prettyPhoto(?:\\.min)?\\.css|<a [^>]*rel=\"prettyPhoto)",
            "icon": "prettyPhoto.png",
            "implies": "jQuery",
            "script": "jquery\\.prettyPhoto\\.js",
            "website": "no-margin-for-errors.com/projects/prettyphoto-jquery-lightbox-clone/"
        },
        "punBB": {
            "cats": [
                2
            ],
            "html": "Powered by <a href=\"[^>]+punbb",
            "icon": "punBB.png",
            "implies": "PHP",
            "website": "punbb.informer.com"
        },
        "reCAPTCHA": {
            "cats": [
                16
            ],
            "env": "^Recaptcha$",
            "html": "(?:<div[^>]+id=\"recaptcha_image|<link[^>]+recaptcha|document\\.getElementById\\('recaptcha')",
            "icon": "reCAPTCHA.png",
            "script": "(?:api-secure\\.recaptcha\\.net|recaptcha_ajax\\.js)",
            "website": "recaptcha.net"
        },
        "sIFR": {
            "cats": [
                17
            ],
            "icon": "sIFR.png",
            "script": "sifr\\.js",
            "website": "www.mikeindustries.com/blog/sifr"
        },
        "sNews": {
            "cats": [
                1
            ],
            "icon": "sNews.png",
            "meta": {
                "generator": "sNews"
            },
            "website": "snewscms.com"
        },
        "script.aculo.us": {
            "cats": [
                12
            ],
            "env": "^Scriptaculous$",
            "icon": "script.aculo.us.png",
            "script": "(?:scriptaculous|protoaculous)\\.js",
            "website": "script.aculo.us"
        },
        "shine.js": {
            "cats": [
                25
            ],
            "env": "^Shine$",
            "icon": "default.png",
            "script": "shine(?:\\.min)?\\.js",
            "website": "bigspaceship.github.io/shine.js/"
        },
        "spin.js": {
            "cats": [
                12,
                25
            ],
            "env": "^Spinner$",
            "icon": "spin.js.png",
            "script": "spin(?:\\.min)?\\.js",
            "website": "fgnass.github.io/spin.js/"
        },
        "swift.engine": {
            "cats": [
                1
            ],
            "headers": {
                "X-Powered-By": "swift\\.engine"
            },
            "icon": "swift.engine.png",
            "website": "mittec.ru/default"
        },
        "three.js": {
            "cats": [
                25
            ],
            "env": "^THREE$",
            "icon": "three.js.png",
            "script": "three(?:\\.min)?\\.js",
            "website": "threejs.org"
        },
        "thttpd": {
            "cats": [
                22
            ],
            "headers": {
                "Server": "\bthttpd(?:/([\\d.]+))?\\;version:\\1"
            },
            "icon": "thttpd.png",
            "website": "acme.com/software/thttpd"
        },
        "total.js": {
            "cats": [
                18
            ],
            "headers": {
                "X-Powered-By": "^total\\.js"
            },
            "icon": "total.js.png",
            "implies": "Node.js",
            "website": "totaljs.com"
        },
        "uCore": {
            "cats": [
                1,
                18
            ],
            "headers": {
                "Set-Cookie": "ucore"
            },
            "icon": "uCore.png",
            "implies": "PHP",
            "meta": {
                "generator": "uCore PHP Framework"
            },
            "website": "ucore.io"
        },
        "uKnowva": {
            "cats": [
                1,
                2,
                18,
                50
            ],
            "headers": {
                "X-Content-Encoded-By": "uKnowva ([\\d.]+)\\;version:\\1"
            },
            "html": "<a[^>]+>Powered by uKnowva</a>",
            "icon": "uKnowva.png",
            "implies": "PHP",
            "meta": {
                "generator": "uKnowva (?: ([\\d.]+))?\\;version:\\1"
            },
            "script": "/media/conv/js/jquery.js",
            "website": "uknowva.com"
        },
        "vBulletin": {
            "cats": [
                2
            ],
            "env": "^(?:vBulletin|vB_[^g])",
            "icon": "vBulletin.png",
            "implies": "PHP",
            "meta": {
                "generator": "vBulletin"
            },
            "website": "www.vbulletin.com"
        },
        "viennaCMS": {
            "cats": [
                1
            ],
            "html": "powered by <a href=\"[^>]+viennacms",
            "icon": "default.png",
            "website": "www.viennacms.nl"
        },
        "vis.js": {
            "cats": [
                25
            ],
            "env": "^vis$",
            "html": "<link[^>]+?href=\"[^\"]+vis(?:\\.min)?\\.css",
            "icon": "vis.js.png",
            "script": "vis(?:\\.min)?\\.js",
            "website": "visjs.org"
        },
        "webEdition": {
            "cats": [
                1
            ],
            "icon": "webEdition.png",
            "meta": {
                "DC.title": "webEdition",
                "generator": "webEdition"
            },
            "website": "webedition.de/en"
        },
        "webpack": {
            "cats": [
                44
            ],
            "env": "^webpackJsonp$",
            "icon": "webpack.svg",
            "website": "webpack.github.io"
        },
        "xCharts": {
            "cats": [
                25
            ],
            "env": "^xChart$",
            "html": "<link[^>]* href=\"[^\"]*xcharts(?:\\.min)?\\.css",
            "icon": "default.png",
            "implies": "D3",
            "script": "xcharts\\.js",
            "website": "tenxer.github.io/xcharts/"
        },
        "xtCommerce": {
            "cats": [
                6
            ],
            "html": "<div class=\"copyright\">[^<]+<a[^>]+>xt:Commerce",
            "icon": "xtCommerce.png",
            "meta": {
                "generator": "xt:Commerce"
            },
            "website": "www.xt-commerce.com"
        },
        "xui": {
            "cats": [
                26,
                12
            ],
            "env": "^xui$",
            "icon": "xui.png",
            "script": "[^a-z]xui.*\\.js",
            "website": "xuijs.com"
        }
    },
    "categories": {
        "1": "CMS",
        "2": "Message Boards",
        "3": "Database Managers",
        "4": "Documentation Tools",
        "5": "Widgets",
        "6": "Ecommerce",
        "7": "Photo Galleries",
        "8": "Wikis",
        "9": "Hosting Panels",
        "10": "Analytics",
        "11": "Blogs",
        "12": "Javascript Frameworks",
        "13": "Issue Trackers",
        "14": "Video Players",
        "15": "Comment Systems",
        "16": "Captchas",
        "17": "Font Scripts",
        "18": "Web Frameworks",
        "19": "Miscellaneous",
        "20": "Editors",
        "21": "LMS",
        "22": "Web Servers",
        "23": "Cache Tools",
        "24": "Rich Text Editors",
        "25": "Javascript Graphics",
        "26": "Mobile Frameworks",
        "27": "Programming Languages",
        "28": "Operating Systems",
        "29": "Search Engines",
        "30": "Web Mail",
        "31": "CDN",
        "32": "Marketing Automation",
        "33": "Web Server Extensions",
        "34": "Databases",
        "35": "Maps",
        "36": "Advertising Networks",
        "37": "Network Devices",
        "38": "Media Servers",
        "39": "Webcams",
        "40": "Printers",
        "41": "Payment Processors",
        "42": "Tag Managers",
        "43": "Paywalls",
        "44": "Build CI Systems",
        "45": "Control Systems",
        "46": "Remote Access",
        "47": "Dev Tools",
        "48": "Network Storage",
        "49": "Feed Readers",
        "50": "Document Management Systems",
        "51": "Landing Page Builders"
    }
}