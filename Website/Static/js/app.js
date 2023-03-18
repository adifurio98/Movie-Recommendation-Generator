$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});




// call Flask API endpoint
function makePredictions() {
    var budget = $("#budget").val();
    var popularity = $("#popularity").val();
    var revenue = $("#revenue").val();
    var runtime = $("#runtime").val();
    var vote_count = $("#vote_count").val();
    var release_year = $("#release_year").val();
    var release_month = $("#release_month").val();
    var release_is_weekend = $("#release_is_weekend").val();
    var genre = $("#genre").val();
    var production_company = $("#production_company").val();
    var production_country = $("#production_country").val();
    var spoken_language = $("#spoken_language").val();


    // check if inputs are valid

    // create the payload
    var payload = {
        "budget": budget,
        "popularity": popularity,
        "revenue": revenue,
        "runtime": runtime,
        "vote_count": vote_count,
        "release_year": release_year,
        "release_month": release_month,
        "release_is_weekend": release_is_weekend,
        "genre": genre,
        "production_company": production_company,
        "production_country": production_country,
        "spoken_language": spoken_language
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);

            if (returnedData["good_prob"] >0.5) {
                $("#output").text("You made a good movie!");
            } else {
                $("#output").text("You did not make a good movie, sorry. :(");
            }
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}