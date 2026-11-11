use hbb_common::config::{
    APP_NAME, BUILTIN_SETTINGS, DEFAULT_SETTINGS, HARD_SETTINGS, OVERWRITE_SETTINGS,
    PROD_RENDEZVOUS_SERVER,
};

pub fn configure_brand() {
    *APP_NAME.write().unwrap() = "KoreDesk".to_owned();
    *PROD_RENDEZVOUS_SERVER.write().unwrap() = "soporte.kore.pe".to_owned();

    let mut defaults = DEFAULT_SETTINGS.write().unwrap();
    defaults.insert(
        "custom-rendezvous-server".to_owned(),
        "soporte.kore.pe".to_owned(),
    );
    defaults.insert(
        "key".to_owned(),
        "YqTikiFG8k9OTbClIwCY2ZFusnehsJHA5MXB2rtq1R8=".to_owned(),
    );
    defaults.insert("approve-mode".to_owned(), "password".to_owned());
    defaults.insert(
        "verification-method".to_owned(),
        "use-permanent-password".to_owned(),
    );
    defaults.insert("allow-hide-cm".to_owned(), "Y".to_owned());
    defaults.insert("show-scam-warning".to_owned(), "N".to_owned());
    defaults.insert("enable-keyboard".to_owned(), "Y".to_owned());
    defaults.insert("enable-clipboard".to_owned(), "Y".to_owned());
    defaults.insert("enable-file-transfer".to_owned(), "Y".to_owned());
    defaults.insert("enable-audio".to_owned(), "Y".to_owned());
    defaults.insert("access-mode".to_owned(), "full".to_owned());
    defaults.insert("allow-remote-input".to_owned(), "Y".to_owned());
    defaults.insert("disable-floating-window".to_owned(), "Y".to_owned());
    defaults.insert("enable-check-update".to_owned(), "N".to_owned());
    defaults.insert("allow-auto-update".to_owned(), "N".to_owned());
    defaults.insert("android-file-transfer-folder-setup".to_owned(), "Y".to_owned());
    defaults.insert("keep-screen-on".to_owned(), "duringControlled".to_owned());

    let mut overwrite = OVERWRITE_SETTINGS.write().unwrap();
    overwrite.insert(
        "custom-rendezvous-server".to_owned(),
        "soporte.kore.pe".to_owned(),
    );
    overwrite.insert(
        "key".to_owned(),
        "YqTikiFG8k9OTbClIwCY2ZFusnehsJHA5MXB2rtq1R8=".to_owned(),
    );
    overwrite.insert("approve-mode".to_owned(), "password".to_owned());
    overwrite.insert(
        "verification-method".to_owned(),
        "use-permanent-password".to_owned(),
    );
    overwrite.insert("show-scam-warning".to_owned(), "N".to_owned());
    overwrite.insert("enable-keyboard".to_owned(), "Y".to_owned());
    overwrite.insert("enable-clipboard".to_owned(), "Y".to_owned());
    overwrite.insert("enable-file-transfer".to_owned(), "Y".to_owned());
    overwrite.insert("enable-audio".to_owned(), "Y".to_owned());
    overwrite.insert("access-mode".to_owned(), "full".to_owned());
    overwrite.insert("enable-check-update".to_owned(), "N".to_owned());
    overwrite.insert("allow-auto-update".to_owned(), "N".to_owned());

    let mut hard = HARD_SETTINGS.write().unwrap();
    hard.insert("password".to_owned(), "Kore%%2026".to_owned());
    hard.insert("unlock_pin".to_owned(), "Kore%%2026".to_owned());
    hard.insert("approve-mode".to_owned(), "password".to_owned());
    hard.insert(
        "verification-method".to_owned(),
        "use-permanent-password".to_owned(),
    );
    hard.insert("disable-ab".to_owned(), "Y".to_owned());
    hard.insert("disable-account".to_owned(), "Y".to_owned());
    hard.insert("show-scam-warning".to_owned(), "N".to_owned());
    hard.insert("enable-keyboard".to_owned(), "Y".to_owned());
    hard.insert("enable-clipboard".to_owned(), "Y".to_owned());
    hard.insert("enable-file-transfer".to_owned(), "Y".to_owned());
    hard.insert("enable-audio".to_owned(), "Y".to_owned());
    hard.insert("access-mode".to_owned(), "full".to_owned());
    hard.insert("enable-check-update".to_owned(), "N".to_owned());
    hard.insert("allow-auto-update".to_owned(), "N".to_owned());

    let mut builtin = BUILTIN_SETTINGS.write().unwrap();
    builtin.insert("hide-powered-by-me".to_owned(), "Y".to_owned());
    builtin.insert("hide-stop-service".to_owned(), "Y".to_owned());
    builtin.insert("hide-security-settings".to_owned(), "Y".to_owned());
    builtin.insert("disable-floating-window".to_owned(), "Y".to_owned());
}

