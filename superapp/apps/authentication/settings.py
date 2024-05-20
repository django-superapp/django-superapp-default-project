def extend_superapp_settings(main_settings):
    main_settings['INSTALLED_APPS'] += [
        'guardian',
        'superapp.apps.authentication',
    ]
    main_settings['GUARDIAN_MONKEY_PATCH'] = False
    main_settings['AUTH_USER_MODEL'] = "authentication.User"
    main_settings['AUTHENTICATION_BACKENDS'] = [
        "superapp.apps.authentication.backend.EmailBackend",
        "django.contrib.auth.backends.ModelBackend",
        "guardian.backends.ObjectPermissionBackend"
    ]
    main_settings['AUTH_PASSWORD_VALIDATORS'] = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]
