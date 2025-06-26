from bs4 import BeautifulSoup

html_code = """<!DOCTYPE html>

<html lang="en">
<head>
<meta content="Cricket News | ICC" name="twitter:title"/>
<meta content="website" property="og:type"/>
<meta content="summary_large_image" property="twitter:card"/>
<meta content="Official source of ICC Cricket news, highlights, match reports, commentary, live scores, fixtures, videos and photos. Top stories, team rankings and more." name="description"/>
<meta content="@icc" property="twitter:site"/>
<meta content="Official source of ICC Cricket news, highlights, match reports, commentary, live scores, fixtures, videos and photos. Top stories, team rankings and more." name="twitter:description"/>
<meta content="https://www.icc-cricket.com/resources/ver/i/elements/default-thumbnail.jpg" name="twitter:image"/>
<meta content="Cricket News | ICC" property="og:title"/>
<meta content="https://www.icc-cricket.com/resources/ver/i/elements/default-thumbnail.jpg" property="og:image"/>
<title>Cricket News | ICC</title>
<meta content="Official source of ICC Cricket news, highlights, match reports, commentary, live scores, fixtures, videos and photos. Top stories, team rankings and more." property="og:description"/>
<!-- Designed and built by Pulselive - www.pulselive.com -->
<script>

    var dataLayer = [{
        'user_language':'English',
        'web_domain':'www.icc-cricket.com',
        'page_type':'/news'  
    }];

</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-T7DPH24');</script>
<!-- End Google Tag Manager -->
<script async="" src="https://securepubads.g.doubleclick.net/tag/js/gpt.js"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1" name="viewport"/>
<meta content="app-id=956440606" name="apple-itunes-app">
<link href="/resources/prod/v8.33.0/manifest.json" rel="manifest"/>
<link href="/resources/prod/v8.33.0/i/elements/favicon.ico" rel="shortcut icon">
<link href="https://plus.google.com/+ICC" rel="publisher"/>
<script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "headline": "",
        "url": "https://www.icc-cricket.com/news", 
        "creator": ["ICC"]
    }
</script>
<title>International Cricket Council</title>
<!-- google platform library -->
<script async="" defer="" src="https://apis.google.com/js/api:client.js?onload=startApp"></script>
<script>

    var startApp = function() {
        gapi.load('auth2', function(){
            // Retrieve the singleton for the GoogleAuth library and set up the client.
            auth2 = gapi.auth2.init({
                client_id: '844310787835-1rirg6e5plp2jou6v701br43iuo0lkcu.apps.googleusercontent.com'
                // Request scopes in addition to 'profile' and 'email'
                //scope: 'additional_scope'
            });
        });
    };
</script>
<link href="https://fonts.googleapis.com/css?family=Hind+Siliguri:300,400,500,600" rel="stylesheet"/>
<!-- Polyfill service provided by the FT - https://github.com/Financial-Times/polyfill-service -->
<script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=default,fetch"></script>
<link href="/resources/prod/v8.33.0/styles/screen.css" rel="stylesheet">
<script>
		window.RESOURCE_VERSION = 'prod/v8.33.0';
	</script>
</link></link></meta></head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe height="0" src="https://www.googletagmanager.com/ns.html?id=GTM-T7DPH24" style="display:none;visibility:hidden" width="0"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
<!--
    Start of Floodlight Tag: Please do not removeActivity name of this tag: ICC Website - VisitationURL of the webpage where the tag is expected to be placed: This tag must be placed between the <body> and </body> tags, as close as possible to the opening tag. Creation Date: 10/01/2019
-->
<iframe frameborder="0" height="1" src="https://9282652.fls.doubleclick.net/activityi;src=9282652;type=iccre0;cat=iccwe0;u1=[user_language];u2=[user_country];u3=[page_type];u4=[web_domain];dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;npa=;ord=[SessionID]?" style="display:none" width="1"></iframe>
<!-- End of Floodlight Tag: Please do not remove -->
<script id="parsely-cfg" src="//cdn.parsely.com/keys/icc-cricket.com/p.js"></script>
<script>
    window.fbAsyncInit = function() {
        FB.init({
            appId            : 159513024983374,
            autoLogAppEvents : true,
            xfbml            : true,
            version          : 'v3.0'
        });
    };

    (function(d, s, id){
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) {return;}
        js = d.createElement(s); js.id = id;
        js.src = "https://connect.facebook.net/en_US/sdk.js";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));
</script>
<div class="user-account-overlay js-user-account-overlay"></div>
<section class="user-account js-user-account" data-script="sso_user-account" data-widget="user-account">
<div class="user-account__wrapper js-panel-account u-hide">
<div class="user-account__header">
<div class="user-account__close js-account-slider-close-btn" role="button">
<svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-close" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>
</div>
<div class="user-account__user-wrapper">
<div class="user-account__image">
<img alt="User Image" class="u-hide js-account-user-img" src="#"/>
</div>
<div class="user-account__user-info">
<p class="user-account__user-info__text js-account-user">Name Lastname</p>
<p class="user-account__user-info__profile js-profile-completion-info u-hide">
<svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-alert" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>
                        Profile <span class="js-profile-completion-percentage"></span>% Complete
                    </p>
</div>
</div>
<div class="user-account__tabs-nav js-tabs-wrapper"></div>
</div>
<div class="account-message js-account-message"></div>
<form autocomplete="off" id="user-account" name="user-account">
<div class="user-account__tab" data-ui-tab="My Account">
<div class="user-account__social-wrapper js-social-wrapper u-hide"></div>
<fieldset>
<div class="form-group-multiple">
<div class="form-group">
<label class="form-group__label" for="given_name">First name *</label>
<input class="form-group__element" id="given_name" maxlength="50" name="given_name" pattern="^[A-Za-z-\s]+$" required="" type="text"/>
<p class="js-error form-error"></p>
</div>
<div class="form-group">
<label class="form-group__label" for="family_name">Last name *</label>
<input class="form-group__element" id="family_name" maxlength="50" name="family_name" pattern="[A-Za-z-\s]+$" required="" type="text"/>
<p class="js-error form-error"></p>
</div>
</div>
<div class="form-group-multiple form-group-multiple--with-button">
<div class="form-group is-disabled js-change-email-input">
<label class="form-group__label" for="email">Email address *</label>
<input autocomplete="off" class="form-group__element" disabled="" id="email" maxlength="50" name="email" type="email"/>
<p class="js-error form-error"></p>
<p class="js-email-exists form-error form-error--email">Email address not available.</p>
</div>
<div class="form-group form-group--button">
<button class="form-btn form-btn--outlined js-change-email" novalidate="" type="button">Change Email</button>
</div>
</div>
<div class="form-group-multiple form-group-multiple--with-button js-account-password">
<div class="form-group is-disabled js-change-password-input">
<label class="form-group__label" for="password">Password *</label>
<input autocomplete="off" class="form-group__element" disabled="" id="password" name="password" placeholder="******" type="password"/>
<p class="js-error form-error"></p>
</div>
<div class="form-group form-group--button">
<button class="form-btn form-btn--outlined js-change-password" novalidate="" type="button">Change Password</button>
</div>
</div>
<div class="form-block form-block">
<div class="form-block__label form-block__label--dob">Date of Birth</div>
<div class="form-group-multiple">
<div class="form-group">
<label class="form-group__label" for="day">Day *</label>
<input class="form-group__element" id="day" min="0" name="day" placeholder="dd" required="" type="number"/>
<p class="js-error form-error"></p>
</div>
<div class="form-group">
<label class="form-group__label" for="month">Month *</label>
<input class="form-group__element" id="month" min="0" name="month" placeholder="mm" required="" type="number"/>
<p class="js-error form-error"></p>
</div>
<div class="form-group">
<label class="form-group__label" for="year">Year *</label>
<input class="form-group__element" id="year" min="0" name="year" placeholder="yyyy" required="" type="number"/>
<p class="js-error form-error"></p>
</div>
</div>
<p class="js-date-error form-error form-error--date">The date of birth is not valid</p>
</div>
<div class="form-block" data-dropdown-type="SSO_COUNTRY" data-widget="form-dropdown">
<div class="form-block__label">Country of residence</div>
<div class="form-dropdown js-dropdown-wrapper"></div>
</div>
</fieldset>
</div>
<div class="user-account__tab" data-ui-tab="My Preferences">
<div class="js-account-prefs u-hide">
<fieldset>
<div class="form-block" data-dropdown-type="SSO_TEAM" data-widget="form-dropdown">
<div class="form-block__label">Your favourite team</div>
<div class="form-dropdown js-dropdown-wrapper"></div>
</div>
<div class="js-contact-prefs user-account__contact-prefs-wrapper">
<div class="user-account__alert">
<svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-alert" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>
<span>Sorry, but your contact preferences will take up to 24hrs to update</span>
</div>
<div class="user-account__contact-prefs">
<div class="form-block form-block--no-margin">
<div class="form-group form-group--checkbox">
<input class="form-group__element" id="allow-contacting" name="allow-contacting" type="checkbox"/>
<label class="form-group__label" for="allow-contacting">I'm happy for the ICC to contact me</label>
</div>
<p class="js-error form-error"></p>
</div>
<div class="form-block form-block--no-margin">
<div class="form-group form-group--checkbox">
<input class="form-group__element" id="allow-partner-contacting" name="allow-partner-contacting" type="checkbox"/>
<label class="form-group__label" for="allow-partner-contacting">I'm happy for the ICC's partners to contact me</label>
</div>
<p class="js-error form-error"></p>
</div>
</div>
</div>
</fieldset>
</div>
<div class="overlay__loader__small js-loader-prefs">
    Hold on! Loading your preferences <div class="loader loader--small"></div>
</div>
</div>
<div class="user-account__buttons-wrapper">
<div class="user-account__account-actions js-buttons-wrapper">
<button class="form-btn form-btn--grey is-disabled js-cancel" disabled="">Cancel</button>
<button class="form-btn is-disabled js-submit" disabled="" type="submit">Save Changes</button>
<div class="loader js-loader u-hide"></div>
</div>
<button class="form-btn form-btn--grey js-account-signout u-show-tablet">Sign Out<svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-sign-out" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg></button>
</div>
</form>
</div>
<div class="user-account__wrapper js-panel-account-password u-hide">
<form id="account-edit-password" name="account-edit-password" novalidate="">
<div class="user-account__tabs-wrapper">
<h1 class="overlay__title">
            Edit your password
            <span class="overlay__title__option"><a class="form-cta js-cancel-password" href="#">back</a></span>
</h1>
<div class="form-group form-group--password">
<div class="form-group__password-action js-toggle-password">Show</div>
<label class="form-group__label" for="current-password">Current Password *</label>
<input class="form-group__element" id="current-password" name="current-password" required="" type="password"/>
<p class="js-error form-error"></p>
<p class="js-current-pwd-error form-error form-error--email">Invalid current password</p>
</div>
<a class="form-cta form-cta--right" href="/forgot-password">Forgot password?</a>
<div class="form-block">
<div class="form-group form-group--password">
<div class="form-group__password-action js-toggle-password">Show</div>
<label class="form-group__label" for="new-password">New password *</label>
<input class="form-group__element" id="new-password" name="new-password" required="" type="password"/>
<div class="form-block__verify-password form-block__verify-password--slider js-verify-password">
                    Password must include...
                    <ul class="form-block__verify-list">
<li class="js-verify-length">8 or more characters</li>
<li class="js-verify-letters">At least one upper and lower case letter</li>
<li class="js-verify-number">At least one number or symbol</li>
</ul>
</div>
<p class="js-error form-error"></p>
<p class="js-new-pwd-error form-error form-error--email">The new password needs to be different than the current one.</p>
</div>
</div>
<div class="form-group form-group--password">
<div class="form-group__password-action js-toggle-password">Show</div>
<label class="form-group__label" for="confirm-password">Confirm new password *</label>
<input class="form-group__element" id="confirm-password" name="confirm-password" required="" type="password"/>
<p class="js-error form-error"></p>
<p class="js-confirm-pwd-error form-error form-error--email">The confirmation does not match your new password</p>
</div>
</div>
<div class="user-account__buttons-wrapper">
<div class="user-account__account-actions">
<button class="form-btn form-btn--grey js-cancel-password" type="button">Cancel</button>
<button class="form-btn is-disabled js-submit-password" disabled="" type="submit">Change Password</button>
<div class="loader js-password-loader u-hide"></div>
</div>
</div>
</form>
</div>
</section>
<div class="main-navigation__container js-will-glue">
<!-- header -->
<header class="main-navigation">
<section class="main-navigation__top-bar">
<nav class="site-tabs">
<ul class="site-tabs__list">
<li class="site-tabs__item theme theme-icc is-active">
<a class="site-tabs__link" href="https://www.icc-cricket.com/homepage">
                    ICC Cricket
                </a>
</li>
<li class="site-tabs__item theme theme-cwc">
<a class="site-tabs__link" href="https://www.cricketworldcup.com/" rel="noopener" target="_blank">
                    Men's Cricket World Cup 2023
                </a>
</li>
<li class="site-tabs__item theme theme-wtc">
<a class="site-tabs__link" href="https://www.worldtestchampionship.com/" rel="noopener" target="_blank">
                    World Test Championship
                </a>
</li>
<li class="site-tabs__item theme theme-wt20wc">
<a class="site-tabs__link" href="https://t20worldcup.com/" rel="noopener" target="_blank">
                    Women’s T20 World Cup 2023
                </a>
</li>
<li class="site-tabs__item theme theme-wu19wc">
<a class="site-tabs__link" href="https://www.u19worldcup.com/">
                    U19 Women’s T20 World Cup 2023
                </a>
</li>
</ul></nav>
<div class="sso-nav js-sso-display">
<div class="loader sso-nav__loader">
<div class="loader__ring">
<div></div>
<div></div>
<div></div>
<div></div>
</div>
</div>
</div>
</section>
<section class="main-navigation__wrapper">
<!-- desktop menu -->
<div class="main-navigation__header u-hide-desktop">
<a class="main-navigation__logo" href="/" title="label.returnToHomepage">
<span class="icn icn-logo-icc-nav"></span>
<span class="u-screen-reader">label.ICCHome</span>
</a>
<nav aria-label="Header Navigation" class="main-navigation__desktop-list js-desktop-nav" id="" role="navigation">
<header class="linked-list__header u-show-desktop">
<a class="linked-list__header-search" href="http://icc-cricket.com/search">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-search-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</a>
<span class="js-mobile-nav-btn">
<svg aria-hidden="true" class="icon linked-list__header-close-icn">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-cross" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</span>
</header>
<ul class="linked-list js-dynamic-list">
<li class="linked-list__item">
<a class="linked-list__link" href="/homepage">
                    Home
                </a>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Scores

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Scores
                        </button>
</header>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Men's

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Men's
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="/mens-schedule/list">
                    Fixtures
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/live-cricket/mens-results">
                    Results
                </a>
</li>
</ul>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Women's

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Women's
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="/womens-schedule/list">
                    Fixtures
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/live-cricket/womens-results">
                    Results
                </a>
</li>
</ul>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/live-cricket/live">
                    Live Scores
                </a>
</li>
<li class="linked-list__item linked-list__item--wider u-hide-desktop">
</li>
<li class="linked-list__item linked-list__item--full-width u-hide-desktop">
<div class="main-navigation__social-container">
<nav class="social-follow">
<h6 class="social-follow__title">Follow Us</h6>
<a class="social-follow__item social-follow__item--facebook" href="https://www.facebook.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-facebook-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.facebook</span></a>
<a class="social-follow__item social-follow__item--twitter" href="https://twitter.com/ICC" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-twitter-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.twitter</span>
</a>
<a class="social-follow__item social-follow__item--instagram" href="https://www.instagram.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-instagram-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.instagram</span>
</a>
<a class="social-follow__item social-follow__item--youtube" href="https://www.youtube.com/user/CricketICC?cbrd=1" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-youtube-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.youtube</span>
</a>
</nav>
<svg aria-hidden="true" focusable="false" style="width:0;height:0;position:absolute;">
<lineargradient gradienttransform="rotate(45)" id="instagram" x2="1" y2="1">
<stop offset="0%" stop-color="#4c68d6"></stop>
<stop offset="33%" stop-color="#b22d98"></stop>
<stop offset="65%" stop-color="#e85a50"></stop>
<stop offset="100%" stop-color="#fbbb59"></stop>
</lineargradient>
</svg>
</div>
</li>
</ul>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Rankings

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Rankings
                        </button>
</header>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Men's

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Men's
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/mens/overview">
                    Overview
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/mens/team-rankings">
                    Team Rankings
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/mens/player-rankings">
                    Players Rankings
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/mens/rankings-predictor/test">
                    Team Rankings Predictor
                </a>
</li>
</ul>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Women's

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Women's
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/womens/overview">
                    Overview
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/womens/team-rankings">
                    Team Rankings
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/womens/player-rankings">
                    Player Rankings
                </a>
</li>
</ul>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/mens/player-rankings/comparison">
                    Player Head to Head
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/about">
                    About Rankings
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/faqs">
                    Rankings FAQs
                </a>
</li>
</ul>
</li>
<li class="linked-list__item linked-list__item--wider u-hide-desktop">
</li>
<li class="linked-list__item linked-list__item--full-width u-hide-desktop">
<div class="main-navigation__social-container">
<nav class="social-follow">
<h6 class="social-follow__title">Follow Us</h6>
<a class="social-follow__item social-follow__item--facebook" href="https://www.facebook.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-facebook-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.facebook</span></a>
<a class="social-follow__item social-follow__item--twitter" href="https://twitter.com/ICC" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-twitter-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.twitter</span>
</a>
<a class="social-follow__item social-follow__item--instagram" href="https://www.instagram.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-instagram-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.instagram</span>
</a>
<a class="social-follow__item social-follow__item--youtube" href="https://www.youtube.com/user/CricketICC?cbrd=1" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-youtube-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.youtube</span>
</a>
</nav>
<svg aria-hidden="true" focusable="false" style="width:0;height:0;position:absolute;">
<lineargradient gradienttransform="rotate(45)" id="instagram" x2="1" y2="1">
<stop offset="0%" stop-color="#4c68d6"></stop>
<stop offset="33%" stop-color="#b22d98"></stop>
<stop offset="65%" stop-color="#e85a50"></stop>
<stop offset="100%" stop-color="#fbbb59"></stop>
</lineargradient>
</svg>
</div>
</li>
</ul>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Events

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Events
                        </button>
</header>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Men's Events

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Men's Events
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="https://www.cricketworldcup.com/">
                    ICC Cricket World Cup
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://2022.t20worldcup.com">
                    ICC T20 World Cup
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://www.worldtestchampionship.com/">
                    ICC World Test Championship
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/u19-world-cup/">
                    ICC U19 Cricket World Cup
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/cricket-world-cup-super-league/fixtures">
                    ICC CWC Super League
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/cricket-world-cup-qualifiers-playoff/fixtures">
                    ICC CWC Qualifer Play-off
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/cricket-world-cup-league-two/news">
                    ICC CWC League 2
                </a>
</li>
</ul>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Women's Events

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Women's Events
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="https://www.t20worldcup.com/">
                    ICC T20 World Cup
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://2022.cricketworldcup.com/">
                    ICC Cricket World Cup
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://www.u19worldcup.com/">
                    ICC U19 T20 World Cup
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/womens-championship">
                    ICC Women's Championship
                </a>
</li>
</ul>
</li>
<li class="linked-list__item linked-list__item--wider u-hide-desktop">
</li>
<li class="linked-list__item linked-list__item--full-width u-hide-desktop">
<div class="main-navigation__social-container">
<nav class="social-follow">
<h6 class="social-follow__title">Follow Us</h6>
<a class="social-follow__item social-follow__item--facebook" href="https://www.facebook.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-facebook-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.facebook</span></a>
<a class="social-follow__item social-follow__item--twitter" href="https://twitter.com/ICC" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-twitter-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.twitter</span>
</a>
<a class="social-follow__item social-follow__item--instagram" href="https://www.instagram.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-instagram-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.instagram</span>
</a>
<a class="social-follow__item social-follow__item--youtube" href="https://www.youtube.com/user/CricketICC?cbrd=1" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-youtube-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.youtube</span>
</a>
</nav>
<svg aria-hidden="true" focusable="false" style="width:0;height:0;position:absolute;">
<lineargradient gradienttransform="rotate(45)" id="instagram" x2="1" y2="1">
<stop offset="0%" stop-color="#4c68d6"></stop>
<stop offset="33%" stop-color="#b22d98"></stop>
<stop offset="65%" stop-color="#e85a50"></stop>
<stop offset="100%" stop-color="#fbbb59"></stop>
</lineargradient>
</svg>
</div>
</li>
</ul>
</li>
<li class="linked-list__item">
<a class="linked-list__link is-active" href="/news">
                    News
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/awards/overview">
                    Awards
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/video">
                    Videos
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://icc.tv">
                    ICC.TV
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="http://icc-cricket.com/shop">
                    Shop
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://www.icctravelandtours.com/icc-mens-cricket-world-cup-india-2023/?utm_source=ICC+Website&amp;utm_medium=referral&amp;utm_campaign=ICC+Travel+Link+CWC">
                    Travel
                </a>
</li>
<li class="linked-list__item no-border u-show-desktop">
<span class="linked-list__title">Explore ICC</span>
</li>
<li class="linked-list__item linked-list__item--promo u-show-desktop">
<section class="app-promo">
<div class="app-promo__top">
<span class="app-promo__icon icn icn-app-icon"></span>
<span class="app-promo__text">Download the official ICC App today</span>
</div>
<div class="app-promo__bottom">
<a class="app-promo__cta icn icn-apple-badge" href="https://itunes.apple.com/gb/app/icc-world-twenty20-india-2016/id956440606?mt=8" target="_blank"></a>
<a class="app-promo__cta icn icn-android-badge" href="https://play.google.com/store/apps/details?id=com.pl.cwc_2015&amp;hl=en_GB" target="_blank"></a>
</div>
</section>
</li>
<li class="linked-list__item linked-list__item--social u-show-desktop">
<div class="main-navigation__social-container">
<nav class="social-follow">
<h6 class="social-follow__title">Follow Us</h6>
<a class="social-follow__item social-follow__item--facebook" href="https://www.facebook.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-facebook-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.facebook</span></a>
<a class="social-follow__item social-follow__item--twitter" href="https://twitter.com/ICC" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-twitter-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.twitter</span>
</a>
<a class="social-follow__item social-follow__item--instagram" href="https://www.instagram.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-instagram-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.instagram</span>
</a>
<a class="social-follow__item social-follow__item--youtube" href="https://www.youtube.com/user/CricketICC?cbrd=1" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-youtube-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.youtube</span>
</a>
</nav>
<svg aria-hidden="true" focusable="false" style="width:0;height:0;position:absolute;">
<lineargradient gradienttransform="rotate(45)" id="instagram" x2="1" y2="1">
<stop offset="0%" stop-color="#4c68d6"></stop>
<stop offset="33%" stop-color="#b22d98"></stop>
<stop offset="65%" stop-color="#e85a50"></stop>
<stop offset="100%" stop-color="#fbbb59"></stop>
</lineargradient>
</svg>
</div>
</li>
</ul>
</nav>
<a class="main-navigation__search" href="http://icc-cricket.com/search">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-search-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</a>
<button aria-controls="sidebar-menu" aria-label="Menu" class="hamburger js-sidebar-btn" type="button">
<span class="hamburger__line hamburger__line--top"></span>
<span class="hamburger__line hamburger__line--middle"></span>
<span class="hamburger__line hamburger__line--bottom"></span>
</button>
</div>
<!-- mobile menu -->
<div class="main-navigation__mobile u-show-desktop" data-widget="mobile-navigation">
<a class="main-navigation__logo" href="/" title="label.returnToHomepage">
<span class="icn icn-logo-icc-nav"></span>
<span class="u-screen-reader">label.ICCHome</span>
</a>
<div class="main-navigation__sub-menu">
<nav class="sub-menu">
<a class="sub-menu__link" href="https://www.icc-cricket.com/homepage">
                Home
            </a>
<a class="sub-menu__link" href="https://www.icc-cricket.com/mens-schedule/list">
                Scores
            </a>
<a class="sub-menu__link" href="https://www.icc-cricket.com/rankings/mens/player-rankings/t20i">
                Rankings
            </a>
<a class="sub-menu__link" href="https://www.icc-cricket.com/awards/player-of-the-tournament/">
                Awards
            </a>
</nav>
</div>
<button aria-controls="mobile-menu" aria-label="Menu" class="hamburger js-mobile-nav-btn" type="button">
<span class="hamburger__line hamburger__line--top"></span>
<span class="hamburger__line hamburger__line--middle"></span>
<span class="hamburger__line hamburger__line--bottom"></span>
<span class="u-screen-reader">label.toggleMobileNavigation</span>
</button>
<nav aria-label="Header Navigation" class="main-navigation__mobile-list js-mobile-nav" id="mobile-menu" role="navigation">
<header class="linked-list__header u-show-desktop">
<a class="linked-list__header-search" href="http://icc-cricket.com/search">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-search-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</a>
<span class="js-mobile-nav-btn">
<svg aria-hidden="true" class="icon linked-list__header-close-icn">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-cross" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</span>
</header>
<ul class="linked-list js-dynamic-list">
<li class="linked-list__item">
<a class="linked-list__link" href="/homepage">
                    Home
                </a>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Scores

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Scores
                        </button>
</header>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Men's

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Men's
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="/mens-schedule/list">
                    Fixtures
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/live-cricket/mens-results">
                    Results
                </a>
</li>
</ul>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Women's

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Women's
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="/womens-schedule/list">
                    Fixtures
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/live-cricket/womens-results">
                    Results
                </a>
</li>
</ul>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/live-cricket/live">
                    Live Scores
                </a>
</li>
<li class="linked-list__item linked-list__item--wider u-hide-desktop">
</li>
<li class="linked-list__item linked-list__item--full-width u-hide-desktop">
<div class="main-navigation__social-container">
<nav class="social-follow">
<h6 class="social-follow__title">Follow Us</h6>
<a class="social-follow__item social-follow__item--facebook" href="https://www.facebook.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-facebook-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.facebook</span></a>
<a class="social-follow__item social-follow__item--twitter" href="https://twitter.com/ICC" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-twitter-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.twitter</span>
</a>
<a class="social-follow__item social-follow__item--instagram" href="https://www.instagram.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-instagram-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.instagram</span>
</a>
<a class="social-follow__item social-follow__item--youtube" href="https://www.youtube.com/user/CricketICC?cbrd=1" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-youtube-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.youtube</span>
</a>
</nav>
<svg aria-hidden="true" focusable="false" style="width:0;height:0;position:absolute;">
<lineargradient gradienttransform="rotate(45)" id="instagram" x2="1" y2="1">
<stop offset="0%" stop-color="#4c68d6"></stop>
<stop offset="33%" stop-color="#b22d98"></stop>
<stop offset="65%" stop-color="#e85a50"></stop>
<stop offset="100%" stop-color="#fbbb59"></stop>
</lineargradient>
</svg>
</div>
</li>
</ul>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Rankings

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Rankings
                        </button>
</header>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Men's

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Men's
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/mens/overview">
                    Overview
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/mens/team-rankings">
                    Team Rankings
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/mens/player-rankings">
                    Players Rankings
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/mens/rankings-predictor/test">
                    Team Rankings Predictor
                </a>
</li>
</ul>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Women's

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Women's
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/womens/overview">
                    Overview
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/womens/team-rankings">
                    Team Rankings
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/womens/player-rankings">
                    Player Rankings
                </a>
</li>
</ul>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/mens/player-rankings/comparison">
                    Player Head to Head
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/about">
                    About Rankings
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/rankings/faqs">
                    Rankings FAQs
                </a>
</li>
</ul>
</li>
<li class="linked-list__item linked-list__item--wider u-hide-desktop">
</li>
<li class="linked-list__item linked-list__item--full-width u-hide-desktop">
<div class="main-navigation__social-container">
<nav class="social-follow">
<h6 class="social-follow__title">Follow Us</h6>
<a class="social-follow__item social-follow__item--facebook" href="https://www.facebook.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-facebook-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.facebook</span></a>
<a class="social-follow__item social-follow__item--twitter" href="https://twitter.com/ICC" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-twitter-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.twitter</span>
</a>
<a class="social-follow__item social-follow__item--instagram" href="https://www.instagram.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-instagram-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.instagram</span>
</a>
<a class="social-follow__item social-follow__item--youtube" href="https://www.youtube.com/user/CricketICC?cbrd=1" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-youtube-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.youtube</span>
</a>
</nav>
<svg aria-hidden="true" focusable="false" style="width:0;height:0;position:absolute;">
<lineargradient gradienttransform="rotate(45)" id="instagram" x2="1" y2="1">
<stop offset="0%" stop-color="#4c68d6"></stop>
<stop offset="33%" stop-color="#b22d98"></stop>
<stop offset="65%" stop-color="#e85a50"></stop>
<stop offset="100%" stop-color="#fbbb59"></stop>
</lineargradient>
</svg>
</div>
</li>
</ul>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Events

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Events
                        </button>
</header>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Men's Events

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Men's Events
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="https://www.cricketworldcup.com/">
                    ICC Cricket World Cup
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://2022.t20worldcup.com">
                    ICC T20 World Cup
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://www.worldtestchampionship.com/">
                    ICC World Test Championship
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/u19-world-cup/">
                    ICC U19 Cricket World Cup
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/cricket-world-cup-super-league/fixtures">
                    ICC CWC Super League
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/cricket-world-cup-qualifiers-playoff/fixtures">
                    ICC CWC Qualifer Play-off
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/cricket-world-cup-league-two/news">
                    ICC CWC League 2
                </a>
</li>
</ul>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    Women's Events

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            Women's Events
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="https://www.t20worldcup.com/">
                    ICC T20 World Cup
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://2022.cricketworldcup.com/">
                    ICC Cricket World Cup
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://www.u19worldcup.com/">
                    ICC U19 T20 World Cup
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/womens-championship">
                    ICC Women's Championship
                </a>
</li>
</ul>
</li>
<li class="linked-list__item linked-list__item--wider u-hide-desktop">
</li>
<li class="linked-list__item linked-list__item--full-width u-hide-desktop">
<div class="main-navigation__social-container">
<nav class="social-follow">
<h6 class="social-follow__title">Follow Us</h6>
<a class="social-follow__item social-follow__item--facebook" href="https://www.facebook.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-facebook-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.facebook</span></a>
<a class="social-follow__item social-follow__item--twitter" href="https://twitter.com/ICC" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-twitter-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.twitter</span>
</a>
<a class="social-follow__item social-follow__item--instagram" href="https://www.instagram.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-instagram-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.instagram</span>
</a>
<a class="social-follow__item social-follow__item--youtube" href="https://www.youtube.com/user/CricketICC?cbrd=1" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-youtube-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.youtube</span>
</a>
</nav>
<svg aria-hidden="true" focusable="false" style="width:0;height:0;position:absolute;">
<lineargradient gradienttransform="rotate(45)" id="instagram" x2="1" y2="1">
<stop offset="0%" stop-color="#4c68d6"></stop>
<stop offset="33%" stop-color="#b22d98"></stop>
<stop offset="65%" stop-color="#e85a50"></stop>
<stop offset="100%" stop-color="#fbbb59"></stop>
</lineargradient>
</svg>
</div>
</li>
</ul>
</li>
<li class="linked-list__item">
<a class="linked-list__link is-active" href="/news">
                    News
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/awards/overview">
                    Awards
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/video">
                    Videos
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://icc.tv">
                    ICC.TV
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="http://icc-cricket.com/shop">
                    Shop
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://www.icctravelandtours.com/icc-mens-cricket-world-cup-india-2023/?utm_source=ICC+Website&amp;utm_medium=referral&amp;utm_campaign=ICC+Travel+Link+CWC">
                    Travel
                </a>
</li>
<li class="linked-list__item has-children">
<button aria-haspopup="true" class="linked-list__dropdown-label js-dropdown-btn">
                    More

	<svg aria-hidden="true" class="icon linked-list__dropdown-has-children">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</button>
<ul aria-expanded="false" aria-hidden="true" class="linked-list__dropdown" role="group">
<header class="linked-list__dropdown-header u-show-desktop">
<button aria-label="Return to previous menu level" class="linked-list__back-btn js-back-btn">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-right-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
                            More
                        </button>
</header>
<li class="linked-list__item">
<a class="linked-list__link" href="/teams">
                    Teams
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/100percentcricket">
                    100% Cricket
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://fancraze.com/">
                    Crictos
	<svg aria-hidden="true" class="icon external-link">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-external-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/awards/overview">
                    ICC Awards
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/hall-of-fame">
                    Hall of Fame
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/about/integrity/anti-doping/code">
                    Anti-doping
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://www.criiio.com/">
                    criiio
	<svg aria-hidden="true" class="icon external-link">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-external-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/mobile">
                    Official ICC App
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/about">
                    About ICC
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="https://www.icc-cricket.com/media-zone">
                    Online Media Zone
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/media-releases">
                    Media Releases
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/photos">
                    Photos
                </a>
</li>
<li class="linked-list__item">
<a class="linked-list__link" href="/news/318971">
                    Commercial Opportunities
                </a>
</li>
<li class="linked-list__item linked-list__item--wider u-hide-desktop">
</li>
<li class="linked-list__item linked-list__item--full-width u-hide-desktop">
<div class="main-navigation__social-container">
<nav class="social-follow">
<h6 class="social-follow__title">Follow Us</h6>
<a class="social-follow__item social-follow__item--facebook" href="https://www.facebook.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-facebook-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.facebook</span></a>
<a class="social-follow__item social-follow__item--twitter" href="https://twitter.com/ICC" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-twitter-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.twitter</span>
</a>
<a class="social-follow__item social-follow__item--instagram" href="https://www.instagram.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-instagram-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.instagram</span>
</a>
<a class="social-follow__item social-follow__item--youtube" href="https://www.youtube.com/user/CricketICC?cbrd=1" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-youtube-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.youtube</span>
</a>
</nav>
<svg aria-hidden="true" focusable="false" style="width:0;height:0;position:absolute;">
<lineargradient gradienttransform="rotate(45)" id="instagram" x2="1" y2="1">
<stop offset="0%" stop-color="#4c68d6"></stop>
<stop offset="33%" stop-color="#b22d98"></stop>
<stop offset="65%" stop-color="#e85a50"></stop>
<stop offset="100%" stop-color="#fbbb59"></stop>
</lineargradient>
</svg>
</div>
</li>
</ul>
</li>
<li class="linked-list__item no-border u-show-desktop">
<span class="linked-list__title">Explore ICC</span>
</li>
<li class="linked-list__item no-border theme theme-wt20wc">
<a class="linked-list__link" href="https://womens.t20worldcup.com/">
                    Women’s T20 World Cup 2023
	<svg aria-hidden="true" class="icon external-link">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-external-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</a>
</li>
<li class="linked-list__item no-border theme theme-wu19wc">
<a class="linked-list__link" href="https://www.u19worldcup.com/">
                    U19 Women’s T20 World Cup 2023
	<svg aria-hidden="true" class="icon external-link">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-external-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</a>
</li>
<li class="linked-list__item no-border theme theme-wtc">
<a class="linked-list__link" href="https://www.icc-cricket.com/world-test-championship/overview">
                    World Test Championship
	<svg aria-hidden="true" class="icon external-link">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-external-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</a>
</li>
<li class="linked-list__item linked-list__item--promo u-show-desktop">
<section class="app-promo">
<div class="app-promo__top">
<span class="app-promo__icon icn icn-app-icon"></span>
<span class="app-promo__text">Download the official ICC App today</span>
</div>
<div class="app-promo__bottom">
<a class="app-promo__cta icn icn-apple-badge" href="https://itunes.apple.com/gb/app/icc-world-twenty20-india-2016/id956440606?mt=8" target="_blank"></a>
<a class="app-promo__cta icn icn-android-badge" href="https://play.google.com/store/apps/details?id=com.pl.cwc_2015&amp;hl=en_GB" target="_blank"></a>
</div>
</section>
</li>
<li class="linked-list__item linked-list__item--social u-show-desktop">
<div class="main-navigation__social-container">
<nav class="social-follow">
<h6 class="social-follow__title">Follow Us</h6>
<a class="social-follow__item social-follow__item--facebook" href="https://www.facebook.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-facebook-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.facebook</span></a>
<a class="social-follow__item social-follow__item--twitter" href="https://twitter.com/ICC" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-twitter-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.twitter</span>
</a>
<a class="social-follow__item social-follow__item--instagram" href="https://www.instagram.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-instagram-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.instagram</span>
</a>
<a class="social-follow__item social-follow__item--youtube" href="https://www.youtube.com/user/CricketICC?cbrd=1" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-youtube-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.youtube</span>
</a>
</nav>
<svg aria-hidden="true" focusable="false" style="width:0;height:0;position:absolute;">
<lineargradient gradienttransform="rotate(45)" id="instagram" x2="1" y2="1">
<stop offset="0%" stop-color="#4c68d6"></stop>
<stop offset="33%" stop-color="#b22d98"></stop>
<stop offset="65%" stop-color="#e85a50"></stop>
<stop offset="100%" stop-color="#fbbb59"></stop>
</lineargradient>
</svg>
</div>
</li>
</ul>
</nav>
</div>
</section>
<!-- sidebar menu -->
<div class="sidebar-nav js-navigation-sidebar u-hide-desktop" data-widget="sidebar-navigation">
<header class="sidebar-nav__header">
<span class="sidebar-nav__title">
                    More
                </span>
<span class="sidebar-nav__close js-sidebar-btn">
<svg aria-hidden="true" class="icon sidebar-nav__close-icn">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-cross" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</span>
</header>
<div class="sidebar-nav__menu" tabindex="0">
<ul>
<li class="sidebar-nav__item" data-label="Teams">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="/teams">
                                Teams
                            </a>
</li>
<li class="sidebar-nav__item" data-label="100% Cricket">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="/100percentcricket">
                                100% Cricket
                            </a>
</li>
<li class="sidebar-nav__item" data-label="Crictos">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="https://fancraze.com/">
                                Crictos
	<svg aria-hidden="true" class="icon external-link">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-external-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</a>
</li>
<li class="sidebar-nav__item" data-label="ICC Awards">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="/awards/overview">
                                ICC Awards
                            </a>
</li>
<li class="sidebar-nav__item" data-label="Hall of Fame">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="/hall-of-fame">
                                Hall of Fame
                            </a>
</li>
<li class="sidebar-nav__item" data-label="Anti-doping">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="/about/integrity/anti-doping/code">
                                Anti-doping
                            </a>
</li>
<li class="sidebar-nav__item" data-label="criiio">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="https://www.criiio.com/">
                                criiio
	<svg aria-hidden="true" class="icon external-link">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-external-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
</a>
</li>
<li class="sidebar-nav__item" data-label="Official ICC App">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="/mobile">
                                Official ICC App
                            </a>
</li>
<li class="sidebar-nav__item" data-label="About ICC">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="/about">
                                About ICC
                            </a>
</li>
<li class="sidebar-nav__item" data-label="Online Media Zone">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="https://www.icc-cricket.com/media-zone">
                                Online Media Zone
                            </a>
</li>
<li class="sidebar-nav__item" data-label="Media Releases">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="/media-releases">
                                Media Releases
                            </a>
</li>
<li class="sidebar-nav__item" data-label="Photos">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="/photos">
                                Photos
                            </a>
</li>
<li class="sidebar-nav__item" data-label="Commercial Opportunities">
<a class="sidebar-nav__link sidebar-nav__link--in-sidebar-nav" href="/news/318971">
                                Commercial Opportunities
                            </a>
</li>
</ul>
</div>
</div>
</header>
</div>
<main class="js-body-content" id="main-content" tabindex="0">
<header class="page-header">
<div class="wrapper">
<div class="col-12">
<div class="page-header__banner">
<h1 class="page-title">News </h1>
</div>
<div class="share share-- share--vertical" data-widget="share">
<div class="share__container">
<div class="share__btn js-share-btn">
<svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-share" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>
<div class="share__title">Share</div>
</div>
<ul class="share__list">
<li class="share__item share__item--facebook js-social-option" data-social-service="facebook" role="button" tabindex="0">
<svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-facebook" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>
</li>
<li class="share__item share__item--twitter js-social-option" data-social-service="twitter" role="button" tabindex="0">
<svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-twitter" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>
</li>
<li class="share__item share__item--messenger u-show-tablet js-social-option" data-social-service="facebookMessenger" role="buttn" tabindex="0">
<svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-facebook-messenger" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>
</li>
<li class="share__item share__item--whatsapp u-show-tablet js-social-option" data-social-service="whatsapp" role="button" tabindex="0">
<svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-whatsapp" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>
</li>
<li class="share__item share__item--url u-hide-tablet js-copy-button" role="button" tabindex="0">
<svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-url" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>
<div class="share__copy-message js-copy-message">URL Copied</div>
</li>
</ul>
</div>
</div>
</div>
</div>
</header>
<div class="wrapper">
<div class="col-12">
</div>
<div class="col-9 col-8-desk col-12-tab has-sidebar">
<section class="widget news-index" data-filter="ALL_TEAM" data-num-pages="1,354" data-page="0" data-page-size="13" data-page-size-loadmore="13" data-references="" data-restricted-content="false" data-script="icc_content-list" data-show-more="true" data-tags="News" data-type="article-hero-list" data-widget="content-list">
<section data-content-filter=""></section>
<section class="sticky-hero-list u-negative-wrapper uniform-grid" data-content-list="">
<div class="sticky-hero-list__wrapper">
<div class="sticky-hero-list__column sticky-hero-list__column--primary">
<a class="thumbnail thumbnail--hero thumbnail--hero thumbnail--sticky-hero" href="/news/3773100">
<figure class="thumbnail__container">
<picture class="thumbnail__picture">
<source srcset="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/08/18afc608-6b55-42ce-95e5-a1e3f2defe82/GFX-for-Marty-article.png?width=500&amp;height=500, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/08/18afc608-6b55-42ce-95e5-a1e3f2defe82/GFX-for-Marty-article.png?width=1000&amp;height=1000 2x"/>
<img alt="Ten of the best: How Maxwell's unforgettable knock compares with other ODI classics" class="thumbnail__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/08/18afc608-6b55-42ce-95e5-a1e3f2defe82/GFX-for-Marty-article.png?width=500&amp;height=500">
</img></picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category">
<svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>
		            CWC23
	            </span>
</div>
<h5 class="thumbnail__title">Ten of the best: How Maxwell's unforgettable knock compares with...</h5>
<div class="thumbnail__summary">Australia star Glenn Maxwell produced one of the all-time great - if not the greatest - innings in a men’s ODI at the ICC Men’s Cricket World Cup. We look at how it compares among 10 of the most memorable knocks in the 50-over format.</div>
<time class="thumbnail__time">
    08 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
<div class="sticky-hero-list__column sticky-hero-list__column--secondary">
<div class="sticky-hero-list__item col-12-phab col-6-tab col-12-desk col-6">
<a class="thumbnail thumbnail--sticky-secondary" href="/news/3773072">
<figure class="thumbnail__container">
<picture class="js-lazy-picture lazy-load thumbnail__picture">
<source data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/08/4a677577-0525-4ce1-8cdb-f27b73e467d3/Maxi-hug.jpg?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/08/4a677577-0525-4ce1-8cdb-f27b73e467d3/Maxi-hug.jpg?width=880&amp;height=495 2x" srcset=""/>
<img alt="" class="thumbnail__image" data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/08/4a677577-0525-4ce1-8cdb-f27b73e467d3/Maxi-hug.jpg?width=440&amp;height=248" src=""/>
</picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category"><svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>CWC23</span>
</div>
<h5 class="thumbnail__title">Cramps, spasms and 201* as Maxwell reveals truth behind superb...</h5>
<time class="thumbnail__time">
    08 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
<div class="sticky-hero-list__item col-12-phab col-6-tab col-12-desk col-6">
<a class="thumbnail thumbnail--sticky-secondary" href="/news/3772836">
<figure class="thumbnail__container">
<picture class="js-lazy-picture lazy-load thumbnail__picture">
<source data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/67a67fcb-cdfa-42bb-b52d-72206bb83c8a/GettyImages-1780447244.jpg?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/67a67fcb-cdfa-42bb-b52d-72206bb83c8a/GettyImages-1780447244.jpg?width=880&amp;height=495 2x" srcset=""/>
<img alt="" class="thumbnail__image" data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/67a67fcb-cdfa-42bb-b52d-72206bb83c8a/GettyImages-1780447244.jpg?width=440&amp;height=248" src=""/>
</picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category"><svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>CWC23</span>
</div>
<h5 class="thumbnail__title">'Un-freaking-believable!' - Cricketers react to Glenn Maxwell's...</h5>
<time class="thumbnail__time">
    07 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
<div class="sticky-hero-list__item col-12-phab col-6-tab col-12-desk col-6">
<a class="thumbnail thumbnail--sticky-secondary" href="/news/3772811">
<figure class="thumbnail__container">
<picture class="js-lazy-picture lazy-load thumbnail__picture">
<source data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/cefb94aa-eef8-46d1-ab4a-af887109f4a4/GettyImages-1780354541.jpg?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/cefb94aa-eef8-46d1-ab4a-af887109f4a4/GettyImages-1780354541.jpg?width=880&amp;height=495 2x" srcset=""/>
<img alt="" class="thumbnail__image" data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/cefb94aa-eef8-46d1-ab4a-af887109f4a4/GettyImages-1780354541.jpg?width=440&amp;height=248" src=""/>
</picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category"><svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>CWC23</span>
</div>
<h5 class="thumbnail__title">Maxwell miracle: Incredible stats behind one of the greatest ODI...</h5>
<time class="thumbnail__time">
    07 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
<div class="sticky-hero-list__item col-12-phab col-6-tab col-12-desk col-6">
<a class="thumbnail thumbnail--sticky-secondary" href="/news/3772606">
<figure class="thumbnail__container">
<picture class="js-lazy-picture lazy-load thumbnail__picture">
<source data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/fea519e8-49f2-467d-b102-ce44888d18ae/AD1_8700_y0E2qcel.JPG?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/fea519e8-49f2-467d-b102-ce44888d18ae/AD1_8700_y0E2qcel.JPG?width=880&amp;height=495 2x" srcset=""/>
<img alt="" class="thumbnail__image" data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/fea519e8-49f2-467d-b102-ce44888d18ae/AD1_8700_y0E2qcel.JPG?width=440&amp;height=248" src=""/>
</picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category"><svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>CWC23</span>
</div>
<h5 class="thumbnail__title">Revealed: Sachin Tendulkar’s advice that inspired Ibrahim...</h5>
<time class="thumbnail__time">
    07 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
<div class="sticky-hero-list__item col-12-phab col-6-tab col-12-desk col-6">
<a class="thumbnail thumbnail--sticky-secondary" href="/news/3772115">
<figure class="thumbnail__container">
<picture class="js-lazy-picture lazy-load thumbnail__picture">
<source data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/72cb3643-671f-458d-869f-2fca3d7010bd/GettyImages-1767325428.jpg?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/72cb3643-671f-458d-869f-2fca3d7010bd/GettyImages-1767325428.jpg?width=880&amp;height=495 2x" srcset=""/>
<img alt="" class="thumbnail__image" data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/72cb3643-671f-458d-869f-2fca3d7010bd/GettyImages-1767325428.jpg?width=440&amp;height=248" src=""/>
</picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category"><svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>CWC23</span>
</div>
<h5 class="thumbnail__title">Bangladesh name replacement for injured Shakib in CWC23 squad</h5>
<time class="thumbnail__time">
    07 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
<div class="sticky-hero-list__item col-12-phab col-6-tab col-12-desk col-6">
<a class="thumbnail thumbnail--sticky-secondary" href="/news/3772006">
<figure class="thumbnail__container">
<picture class="js-lazy-picture lazy-load thumbnail__picture">
<source data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/a5136e27-e5d4-4624-a74d-c13e8ca2d611/Dar-Bangladesh.jpg?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/a5136e27-e5d4-4624-a74d-c13e8ca2d611/Dar-Bangladesh.jpg?width=880&amp;height=495 2x" srcset=""/>
<img alt="" class="thumbnail__image" data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/a5136e27-e5d4-4624-a74d-c13e8ca2d611/Dar-Bangladesh.jpg?width=440&amp;height=248" src=""/>
</picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category"><svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>MRF Tyres ICC Rankings</span>
</div>
<h5 class="thumbnail__title">Pakistan skipper rewarded on latest rankings update</h5>
<time class="thumbnail__time">
    07 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
<div class="sticky-hero-list__item col-12-phab col-6-tab col-12-desk col-6">
<a class="thumbnail thumbnail--sticky-secondary" href="/news/3772047">
<figure class="thumbnail__container">
<picture class="js-lazy-picture lazy-load thumbnail__picture">
<source data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/bcfe38c1-a498-4fd0-b57d-592959dc0138/GettyImages-1768435156.jpg?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/bcfe38c1-a498-4fd0-b57d-592959dc0138/GettyImages-1768435156.jpg?width=880&amp;height=495 2x" srcset=""/>
<img alt="" class="thumbnail__image" data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/bcfe38c1-a498-4fd0-b57d-592959dc0138/GettyImages-1768435156.jpg?width=440&amp;height=248" src=""/>
</picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category"><svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>CWC23</span>
</div>
<h5 class="thumbnail__title">Maxwell's stunning double ton leads Australia into semi-finals</h5>
<time class="thumbnail__time">
    07 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
<div class="sticky-hero-list__item col-12-phab col-6-tab col-12-desk col-6">
<a class="thumbnail thumbnail--sticky-secondary" href="/news/3772017">
<figure class="thumbnail__container">
<picture class="js-lazy-picture lazy-load thumbnail__picture">
<source data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/6432d162-dec1-4456-8870-a22931946406/EngvNED-preview.jpg?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/6432d162-dec1-4456-8870-a22931946406/EngvNED-preview.jpg?width=880&amp;height=495 2x" srcset=""/>
<img alt="" class="thumbnail__image" data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/07/6432d162-dec1-4456-8870-a22931946406/EngvNED-preview.jpg?width=440&amp;height=248" src=""/>
</picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category"><svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>CWC23</span>
</div>
<h5 class="thumbnail__title">England look to salvage something from disappointing World Cup...</h5>
<time class="thumbnail__time">
    07 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
<div class="sticky-hero-list__item col-12-phab col-6-tab col-12-desk col-6">
<a class="thumbnail thumbnail--sticky-secondary thumbnail--wtc" href="/news/3771975">
<figure class="thumbnail__container">
<picture class="js-lazy-picture lazy-load thumbnail__picture">
<source data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/06/d0c42258-7a07-4a37-bac2-25c6e704f99d/Mitchell-Santner-of-New-Zealand-appeals-for-the-wicket-Test-Match-between-England-and-New-Zealand.jpg?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/06/d0c42258-7a07-4a37-bac2-25c6e704f99d/Mitchell-Santner-of-New-Zealand-appeals-for-the-wicket-Test-Match-between-England-and-New-Zealand.jpg?width=880&amp;height=495 2x" srcset=""/>
<img alt="" class="thumbnail__image" data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/06/d0c42258-7a07-4a37-bac2-25c6e704f99d/Mitchell-Santner-of-New-Zealand-appeals-for-the-wicket-Test-Match-between-England-and-New-Zealand.jpg?width=440&amp;height=248" src=""/>
</picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category"><svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>New Zealand news</span>
</div>
<h5 class="thumbnail__title">New Zealand turn to spin as squad named for Test series in...</h5>
<time class="thumbnail__time">
    06 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
<div class="sticky-hero-list__item col-12-phab col-6-tab col-12-desk col-6">
<a class="thumbnail thumbnail--sticky-secondary" href="/news/3771413">
<figure class="thumbnail__container">
<picture class="js-lazy-picture lazy-load thumbnail__picture">
<source data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/06/571182ed-9084-46ad-aaaf-d8e9e1e02b7a/GettyImages-1777985051.jpg?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/06/571182ed-9084-46ad-aaaf-d8e9e1e02b7a/GettyImages-1777985051.jpg?width=880&amp;height=495 2x" srcset=""/>
<img alt="" class="thumbnail__image" data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/06/571182ed-9084-46ad-aaaf-d8e9e1e02b7a/GettyImages-1777985051.jpg?width=440&amp;height=248" src=""/>
</picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category"><svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>CWC23</span>
</div>
<h5 class="thumbnail__title">Mathews, Shakib react to controversial ‘timed out’ dismissal</h5>
<time class="thumbnail__time">
    06 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
<div class="sticky-hero-list__item col-12-phab col-6-tab col-12-desk col-6">
<a class="thumbnail thumbnail--sticky-secondary" href="/news/3771241">
<figure class="thumbnail__container">
<picture class="js-lazy-picture lazy-load thumbnail__picture">
<source data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/06/3c6d6fe6-16c8-454b-afc5-787d94a7980c/AD1_8609_or2avfwe.JPG?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/06/3c6d6fe6-16c8-454b-afc5-787d94a7980c/AD1_8609_or2avfwe.JPG?width=880&amp;height=495 2x" srcset=""/>
<img alt="" class="thumbnail__image" data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/06/3c6d6fe6-16c8-454b-afc5-787d94a7980c/AD1_8609_or2avfwe.JPG?width=440&amp;height=248" src=""/>
</picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category"><svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>CWC23</span>
</div>
<h5 class="thumbnail__title">Sachin Tendulkar addresses inspired Afghanistan ahead of crunch...</h5>
<time class="thumbnail__time">
    06 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
<div class="sticky-hero-list__item col-12-phab col-6-tab col-12-desk col-6">
<a class="thumbnail thumbnail--sticky-secondary" href="/news/3770966">
<figure class="thumbnail__container">
<picture class="js-lazy-picture lazy-load thumbnail__picture">
<source data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/06/6bc6ca11-ef27-409a-945e-3bf101dba661/GettyImages-1766832246.jpg?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/11/06/6bc6ca11-ef27-409a-945e-3bf101dba661/GettyImages-1766832246.jpg?width=880&amp;height=495 2x" srcset=""/>
<img alt="" class="thumbnail__image" data-image-src="https://resources.pulse.icc-cricket.com/photo-resources/2023/11/06/6bc6ca11-ef27-409a-945e-3bf101dba661/GettyImages-1766832246.jpg?width=440&amp;height=248" src=""/>
</picture>
<figcaption class="thumbnail__caption">
<div class="thumbnail__meta">
<span class="thumbnail__category"><svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-article" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>CWC23</span>
</div>
<h5 class="thumbnail__title">Explained: Why Angelo Mathews was dismissed before facing a ball</h5>
<time class="thumbnail__time">
    06 Nov 23

</time>
</figcaption>
</figure>
</a>
</div>
</div>
</div>
</section>
<div class="js-show-more">
<div class="view-more-block js-show-more-button">
<div class="view-more-block__label">Show More</div>
<div class="view-more-block__type">News</div>
<div class="view-more-block__icon">
<svg class="icon"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-chevron-down" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg>
</div>
</div>
<div class="loader js-loader u-hide"></div>
</div>
</section>
</div>
<div class="col-3 col-4-desk col-12-tab is-sidebar">
<section class="tabbed-matches u-hide-tablet" data-match-states="C,U,L" data-match-types="OTHER,T20I,T20,TEST,ODI,FIRST_CLASS,LIST_A" data-page-size="35" data-script="icc_match-list" data-sort="asc" data-team-types="" data-tournament-group-id="" data-tournament-id="" data-tournament-types="WI,I" data-widget="tabbed-matchlist">
<header class="tabbed-matches__header">
<svg class="icon external"><use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-icc-logo" xmlns:xlink="http://www.w3.org/1999/xlink"></use></svg><h3 class="widget__title widget__title--small">Live Cricket</h3>
</header>
<nav class="tabs"></nav>
<div class="tabbed-matches__container wrap-fixtures-abridged">
<div class="tabbed-matches__content js-tabbed-match" data-ui-tab="Live">
<div class="js-matchlist-live"></div>
</div>
<div class="tabbed-matches__content js-tabbed-match" data-ui-tab="Fixtures">
<div class="js-matchlist-fixtures"></div>
</div>
<div class="tabbed-matches__content js-tabbed-match" data-ui-tab="Results">
<div class="js-matchlist-results"></div>
</div>
</div>
<div class="loader js-loader"></div>
</section>
<section class="trending-content">
<header class="trending-content__header">
<h3 class="trending-content__header-title">
                Trending News
            </h3>
</header>
<ul>
<li class="trending-content__item trending-content__item--first-child">
<span class="trending-content__index trending-content__index--alt">1</span>
<a class="trending-content__link" href="/news/3755806">
<figure class="trending-content__container">
<picture>
<source srcset="https://resources.pulse.icc-cricket.com/photo-resources/2023/10/28/c599f773-fb69-463f-b734-85b4e82b7a4a/Pakistan-sanctioned.jpg?width=440&amp;height=248, https://resources.pulse.icc-cricket.com/photo-resources/2023/10/28/c599f773-fb69-463f-b734-85b4e82b7a4a/Pakistan-sanctioned.jpg?width=880&amp;height=495 2x"/>
<img alt="" class="trending-content__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/10/28/c599f773-fb69-463f-b734-85b4e82b7a4a/Pakistan-sanctioned.jpg?width=440&amp;height=248"/>
</picture>
<figcaption class="trending-content__caption">
<span class="trending-content__index">1</span>
<h5 class="trending-content__article-text">Pakistan sanctioned following narrow loss against South Africa</h5>
<p class="trending-content__article-summary">Pakistan's faltering ICC Men's Cricket World Cup campaign has received a further blow with the team sanctioned for a slow over rate during their recent match against South Africa.</p>
</figcaption>
</figure>
</a>
</li>
<li class="trending-content__item">
<a class="trending-content__link" href="/news/3754913">
<figure class="trending-content__container">
<figcaption class="trending-content__caption">
<span class="trending-content__index">2</span>
<h5 class="trending-content__article-text">Laws Explainer: Why Markram wasn’t given out after leaving his ground</h5>
</figcaption>
</figure>
</a>
</li>
<li class="trending-content__item">
<a class="trending-content__link" href="/news/3755637">
<figure class="trending-content__container">
<figcaption class="trending-content__caption">
<span class="trending-content__index">3</span>
<h5 class="trending-content__article-text">World Cup stars included as Australia name T20I squad to play India</h5>
</figcaption>
</figure>
</a>
</li>
<li class="trending-content__item">
<a class="trending-content__link" href="/news/3755707">
<figure class="trending-content__container">
<figcaption class="trending-content__caption">
<span class="trending-content__index">4</span>
<h5 class="trending-content__article-text">Australia beat New Zealand in World Cup epic</h5>
</figcaption>
</figure>
</a>
</li>
<li class="trending-content__item">
<a class="trending-content__link" href="/news/3752830">
<figure class="trending-content__container">
<figcaption class="trending-content__caption">
<span class="trending-content__index">5</span>
<h5 class="trending-content__article-text">World Cup State of Play: Five teams chase two semi-final spots still up for grabs</h5>
</figcaption>
</figure>
</a>
</li>
</ul>
</section>
<section class="mpu mpu--ecal mpu--desktop">
<button class="ecal-widget-button" data-ecal-category="Men,Women">
<span class="ecal-widget-button__text">Add Fixtures to Calendar</span>
</button>
</section>
<section>
<a class="twitter-timeline" data-tweet-limit="2" href="https://twitter.com/ICC?ref_src=twsrc%5Etfw">Tweets by ICC</a> <script async="" charset="utf-8" src="https://platform.twitter.com/widgets.js"></script>
</section>
</div>
</div>
</main>
<footer class="footer" role="contentinfo">
<section class="partners">
<div class="partners__top-level">
<section class="partners__container">
<div class="partners__list partners__list--large">
<div class="partners__item">
<a aria-label="MRF Tyres" class="partners__link" href="http://track.adform.net/C/?bn=18235782" title="MRF Tyres">
<img alt="MRF Tyres" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/05/10/bd67f054-5413-47b1-80e1-03826947a41f/mrf-tyres.png?width=142&amp;height=46"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Booking" class="partners__link" href="https://www.booking.com/" target="_blank" title="Booking">
<img alt="Booking" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2022/06/30/8bb6e96d-2b69-4d8e-acc0-568602baba2d/Frame-234.png?width=142&amp;height=46"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Indusind Bank" class="partners__link" href="https://www.indusind.com/" title="Indusind Bank">
<img alt="Indusind Bank" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/09/27/8113c906-0f4a-4114-a044-f9a599b4d06c/Induslnd_Bank.png?width=142&amp;height=46"/>
</a>
</div>
<div class="partners__item">
<a aria-label="mastercard" class="partners__link" href="https://www.mastercard.com/" title="mastercard">
<img alt="Mastercard" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/08/31/780f5b83-9d69-4138-b679-fe29dfd5a6a9/Mastercard_light.png?width=142&amp;height=46"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Aramco" class="partners__link" href="https://www.aramco.com/" target="_blank" title="Aramco">
<img alt="Aramco" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/01/18/084e1d99-8978-4c9d-96f0-a4aee4395e40/Frame.png?width=142&amp;height=46"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Emirates" class="partners__link" href="http://track.adform.net/C/?bn=18236184" title="Emirates">
<img alt="Emirates" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2022/06/30/d9fb726d-2cbd-41c8-9aaf-bd94f37a8e4a/Frame-236.png?width=142&amp;height=46"/>
</a>
</div>
</div>
</section>
</div>
<div class="partners__block">
<section class="partners__container">
<div class="partners__list partners__list--large">
<div class="partners__item">
<a aria-label="Bira 91" class="partners__link" href="https://shop.bira91.com/?utm_medum=iccweb&amp;utm_campaign=iccworldcup23&amp;utm_source=partnerlogo" target="_blank" title="Bira 91">
<img alt="Bira 91" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/08/31/508f9db6-6f31-4a4b-804f-f7fb1acb867b/bira_Light.png?width=142&amp;height=46"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Polycab" class="partners__link" href="https://polycab.com/" target="_blank" title="Polycab">
<img alt="Polycab" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/09/28/443ef16b-023f-4094-aef5-744c3c6cf67c/Polycab.png?width=142&amp;height=46"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Coca Cola" class="partners__link" href="https://www.coca-colaindia.com/brands/thums-up" title="Coca Cola">
<img alt="Coca Cola" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/09/28/352550fe-ebbb-4e40-a140-d5b85b49fe3d/taste-thunder_outline.png?width=142&amp;height=46"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Upstox" class="partners__link" href="https://upstox.com/" target="_blank" title="Upstox">
<img alt="Upstox" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/09/28/b222e215-671b-41c4-b81e-575e36038e60/upstox_Light.png?width=142&amp;height=46"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Tracking" class="partners__link" href="https://track.adform.net/adfserve/?bn=18235072;srctype=4;ord=%%ADFRND%%" target="_blank" title="Tracking">
<img alt="Nissan" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/08/31/d80133d0-7fe1-4e21-8f11-1b4fb9666f0d/Nissan.png?width=142&amp;height=46"/>
</a>
</div>
<div class="partners__item">
<a aria-label="NIUM" class="partners__link" href="https://www.nium.com/" target="_blank" title="NIUM">
<img alt="NIUM" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/08/31/f3ff47a4-9587-4508-8ca7-fa7ecbadb254/nium_Light.png?width=142&amp;height=46"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Oppo" class="partners__link" href="http://track.adform.net/C/?bn=18236015" target="_blank" title="Oppo">
<img alt="Oppo" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/08/31/7f3abc9c-1512-4732-995e-9a824185e087/oppo_Light.png?width=142&amp;height=46"/>
</a>
</div>
<div class="partners__item">
<a aria-label="DP World" class="partners__link" href="https://www.dpworld.com/" title="DP World">
<img alt="DP World" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/08/31/9cc226c8-1585-44ed-b9bf-3d2fe1dd1149/DP-WORLD_outline.png?width=142&amp;height=46"/>
</a>
</div>
</div>
</section>
<section class="partners__container">
<div class="partners__list partners__list--medium">
<div class="partners__item">
<a aria-label="Royal Stag" class="partners__link" href="https://www.pernod-ricard.com/en/brands/our-brands/royal-stag/" target="_blank" title="Royal Stag">
<img alt="Royal Stag" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/09/27/07e12e17-4204-4e67-8750-ed971d046994/ROYAL-STAG.png?width=95&amp;height=31"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Fantasy Cricket" class="partners__link" href="https://www.dream11.com/fantasy-cricket" target="_blank" title="Fantasy Cricket">
<img alt="Fantasy Cricket" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2022/06/30/d08b4b92-a224-4484-8269-22184d633d74/Frame-248.png?width=95&amp;height=31"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Jacobs Creek" class="partners__link" href="https://www.jacobscreek.com/" target="_blank" title="Jacobs Creek">
<img alt="Jacobs Creek" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/09/27/9516959d-9355-45c1-ae6a-f4d42dda4820/JACOBS-CREEK_LIGHT.png?width=95&amp;height=31"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Near" class="partners__link" href="https://near.org/" title="Near">
<img alt="Near" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/09/29/c25f916c-d046-4595-81b7-439020db39ed/NEAR_LIGHT.png?width=95&amp;height=31"/>
</a>
</div>
<div class="partners__item">
<a aria-label="Mphasis" class="partners__link" href="https://www.mphasis.com/" target="_blank" title="Mphasis">
<img alt="Mphasis_Light" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2023/10/14/6500d606-a7af-4adc-b4aa-0bc616fcd3b5/Mphasis_Light.png?width=95&amp;height=31"/>
</a>
</div>
<div class="partners__item">
<a aria-label="FanCraze" class="partners__link" href="https://www.fancraze.com" title="FanCraze">
<img alt="FanCraze" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2022/06/30/51c3576a-0e91-4246-8d36-85fc5037cec6/Frame-249.png?width=95&amp;height=31"/>
</a>
</div>
<div class="partners__item">
<a aria-label="TYKA" class="partners__link" href="https://tyka.com/global/" title="TYKA">
<img alt="TYKA" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2022/10/14/c2bd7874-c1b0-47d1-ab5d-6e958952ed9a/Tyka.png?width=95&amp;height=31"/>
</a>
</div>
</div>
</section>
</div>
<div class="partners__block partners__block--inline">
<section class="partners__container">
<h3 class="partners__title">BROADCAST PARTNER</h3>
<div class="partners__list partners__list--large">
<div class="partners__item">
<a aria-label="Star Sports" class="partners__link" href="http://track.adform.net/C/?bn=18238489" target="_blank" title="Star Sports">
<img alt="Star Sports" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2022/06/30/6becb07e-9e85-4221-a4cf-43d1b58c5e46/star-sports.png?width=142&amp;height=46"/>
</a>
</div>
</div>
</section>
<section class="partners__container">
<h3 class="partners__title">SOCIAL RESPONSIBILITY</h3>
<div class="partners__list partners__list--large">
<div class="partners__item">
<a aria-label="Cricket for Good" class="partners__link" href="https://www.icc-cricket.com/about/the-icc/cricket-for-good" target="_blank" title="Cricket for Good">
<img alt="Cricket for Good" class="partners__image" src="https://resources.pulse.icc-cricket.com/photo-resources/2022/06/30/66d0bd38-4492-4742-ae2f-a5a2f3ea7032/cricket4good.png?width=142&amp;height=46"/>
</a>
</div>
</div>
</section>
</div>
</section>
<div class="footer__app-promo u-show-tablet">
<section class="app-promo">
<div class="app-promo__top">
<span class="app-promo__icon icn icn-app-icon"></span>
<span class="app-promo__text">Download the official ICC App today</span>
</div>
<div class="app-promo__bottom">
<a class="app-promo__cta icn icn-apple-badge" href="https://itunes.apple.com/gb/app/icc-world-twenty20-india-2016/id956440606?mt=8" target="_blank"></a>
<a class="app-promo__cta icn icn-android-badge" href="https://play.google.com/store/apps/details?id=com.pl.cwc_2015&amp;hl=en_GB" target="_blank"></a>
</div>
</section>
</div>
<div class="footer__main">
<nav class="footer__links">
<a class="footer__link" href="http://www.icc-cricket.com/about/the-icc/legal-notices/website-terms-of-use">
                        Legal Notice
                    </a>
<a class="footer__link" href="http://www.icc-cricket.com/about/the-icc/legal-notices/privacy-policy">
                        Privacy Policy
                    </a>
</nav>
<div class="footer__social">
<nav class="social-follow">
<h6 class="social-follow__title">Follow Us</h6>
<a class="social-follow__item social-follow__item--facebook" href="https://www.facebook.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-facebook-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.facebook</span></a>
<a class="social-follow__item social-follow__item--twitter" href="https://twitter.com/ICC" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-twitter-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.twitter</span>
</a>
<a class="social-follow__item social-follow__item--instagram" href="https://www.instagram.com/icc/" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-instagram-new-hp" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.instagram</span>
</a>
<a class="social-follow__item social-follow__item--youtube" href="https://www.youtube.com/user/CricketICC?cbrd=1" target="_blank">
<svg aria-hidden="true" class="icon">
<use xlink:href="/resources/prod/v8.33.0/i/svg-output/icons.svg#icn-youtube-color" xmlns:xlink="http://www.w3.org/1999/xlink"></use>
</svg>
<span class="u-screen-reader">label.follow.youtube</span>
</a>
</nav>
<svg aria-hidden="true" focusable="false" style="width:0;height:0;position:absolute;">
<lineargradient gradienttransform="rotate(45)" id="instagram" x2="1" y2="1">
<stop offset="0%" stop-color="#4c68d6"></stop>
<stop offset="33%" stop-color="#b22d98"></stop>
<stop offset="65%" stop-color="#e85a50"></stop>
<stop offset="100%" stop-color="#fbbb59"></stop>
</lineargradient>
</svg>
</div>
</div>
<div class="footer__corporate">
<span class="footer__copyright">2023 © International Cricket Council FZ LLC</span>
</div>
</footer>
<section class="cookie-notice" data-script="icc_cookie-notice" data-widget="cookie-notice">
<div class="wrapper">
<div class="col-12 cookie-notice__content-wrapper">
<div class="cookie-notice__info">
<h3 class="cookie-notice__title">Cookie Notice</h3>
<div class="cookie-notice__body"><p>This website employs cookies to improve user experience. If you continue on this website you will be providing your consent to our use of all cookies. <a href="http://www.icc-cricket.com/about/the-icc/legal-notices/privacy-policy">Find out more</a>.</p></div>
</div>
<div class="cookie-notice__button btn js-cookie-btn">Accept</div>
</div>
</div>
</section>
<script src="/resources/prod/v8.33.0/scripts/vendors.min.js"></script>
<script src="/resources/prod/v8.33.0/scripts/client.min.js"></script>
<script src="https://www.icc-cricket.com/resources/keycloak.js"></script>
<!--[if IE]> -->
<script type="text/javascript">
        svg4everybody();
    </script>
<!-- <![endif]-->
</body>
</html>

"""

soup = BeautifulSoup(html_code, 'html.parser')

# Extract information from the HTML document
# For example, to get the title of the page:
title = soup.title.string
print(title)

# You can also extract other elements and their attributes using the BeautifulSoup methods
# For example, to get the image source:
image_src = soup.find('img')['src']
print(image_src)


