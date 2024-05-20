def extend_superapp_settings(main_settings):
    main_settings['INSTALLED_APPS'] += [
        'superapp.apps.sample_app',
    ]
