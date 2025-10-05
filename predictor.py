def main(input_values: dict):
    import joblib
    import pandas as pd
    # When predicting on new data
    feature_cols = joblib.load("feature_cols.pkl")
    new_df = pd.DataFrame([input_values])

    # Reindex to full feature set
    new_df = new_df.reindex(columns=feature_cols)

    # Load and predict
    pipeline = joblib.load("exoplanet_model_v3.pkl")
    best_threshold = joblib.load("threshold.pkl")

    proba = pipeline.predict_proba(new_df)[:, 1][0]
    proba_percent = round(proba * 100, 2)
    prediction = int(proba >= best_threshold)
    return f"Probality: {proba_percent}%", f"Prediction (>= threshold): {prediction}"

if __name__ == "__main__":
    example_input = {'pl_orbper': 21.1791, 'pl_orbpererr1': 0.0030, 'pl_orbpererr2': -0.0027,
                     'pl_orbperlim': 0.0, 'pl_rade': 2.71, 'pl_radeerr1': 0.33, 'pl_radeerr2': -0.37,
                     'pl_radelim': 0.0, 'pl_radj': 0.242, 'pl_radjerr1': 0.029, 'pl_radjerr2': -0.033,
                     'pl_radjlim': 0.0, 'st_teff': 5277.0, 'st_tefferr1': 94.9, 'st_tefferr2': -92.63,
                     'st_tefflim': 0.0, 'st_rad': 1.362, 'st_raderr1': 0.137, 'st_raderr2': -0.039,
                     'st_radlim': 0.0, 'ra': 205.8941425, 'dec': -16.6906686, 'sy_dist': 569.102,
                     'sy_disterr1': 15.007, 'sy_disterr2': -14.268, 'sy_vmag': 13.091, 'sy_vmagerr1': 0.114,
                     'sy_vmagerr2': -0.114, 'sy_kmag': 11.309, 'sy_kmagerr1': 0.021, 'sy_kmagerr2': -0.021,
                     'sy_gaiamag': 12.8021, 'sy_gaiamagerr1': 0.000325, 'sy_gaiamagerr2': -0.000325}
    main(example_input)