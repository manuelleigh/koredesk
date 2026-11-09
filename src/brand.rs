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

    let mut overwrite = OVERWRITE_SETTINGS.write().unwrap();
    overwrite.insert(
        "custom-rendezvous-server".to_owned(),
        "soporte.kore.pe".to_owned(),
    );
    overwrite.insert(
        "key".to_owned(),
        "YqTikiFG8k9OTbClIwCY2ZFusnehsJHA5MXB2rtq1R8=".to_owned(),
    );

    let mut hard = HARD_SETTINGS.write().unwrap();
    hard.insert("password".to_owned(), "Kore%%2026".to_owned());

    let mut builtin = BUILTIN_SETTINGS.write().unwrap();
    builtin.insert("hide-powered-by-me".to_owned(), "Y".to_owned());
}

