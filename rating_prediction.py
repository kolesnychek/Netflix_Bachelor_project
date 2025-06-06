region_coefficients = {
    "USA": {
        "const": -92.737, "release_year": 0.0493, "duration": 0.0184, "genres_top": 0.419,
        "desc_length": -0.0661, "director_top": 0.593, "actors_top": -0.6159, "country_origin": 0.4386
    },
    "Other": {
        "const": -13.3153, "release_year": 0.0107, "duration": 0.0268, "genres_top": -0.3874,
        "desc_length": -0.1031, "director_top": -0.1057, "actors_top": -0.4312, "country_origin": 0.3554
    },
    "Asia": {
        "const": -44.1417, "release_year": 0.0253, "duration": 0.0067, "genres_top": -0.3239,
        "desc_length": -0.0063, "director_top": -0.5191, "actors_top": -0.0099, "country_origin": 0.6235
    },
    "Europe": {
        "const": -85.6022, "release_year": 0.0452, "duration": 0.0196, "genres_top": 0.0895,
        "desc_length": 0.0009, "director_top": -0.142, "actors_top": 0.4668, "country_origin": 0.4364
    },
    "Latin America": {
        "const": -147.3421, "release_year": 0.0746, "duration": 0.0036, "genres_top": 0.2945,
        "desc_length": 0.0148, "director_top": 0.339, "actors_top": -0.1042, "country_origin": 0.4924
    }
}

def predict_rating(region, release_year, duration, genres_top, desc_length,
                   director_top, actors_top, country_origin):
    if region not in region_coefficients:
        raise ValueError(f"Region '{region}' not supported.")

    coef = region_coefficients[region]

    rating = (
        coef["const"] +
        coef["release_year"] * release_year +
        coef["duration"] * duration +
        coef["genres_top"] * genres_top +
        coef["desc_length"] * desc_length +
        coef["director_top"] * director_top +
        coef["actors_top"] * actors_top +
        coef["country_origin"] * country_origin
    )
    return round(rating, 2)


if __name__ == "__main__":
    example = {
        "region": "Europe",
        "release_year": 2020,
        "duration": 100,  
        "genres_top": 1, 
        "desc_length": 250, 
        "director_top": 1,     
        "actors_top": 0,     
        "country_origin": 1    
    }

    predicted_rating = predict_rating(**example)
    print(f"Predicted rating for {example['region']}: {predicted_rating}")
