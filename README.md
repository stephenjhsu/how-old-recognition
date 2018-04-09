# How Old Recommendation (Image to Age Prediction)

![Alt text](../presentation.jpg?raw=true "Presentation of How Old Recommendation")

Creators: Akshay Tiwari, David Kes, Kishan Panchal, Stephen Hsu


## Summary:

This repo contains the code of an Image - to - age predictor for a graduate level Distributed Computing course. 

## Tools: 

Amazon Web Services (S3 and EC2), MongoDB, Spark, Spark ML

## Details:

By using the IMDB face dataset (https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/), we processed the data locally by efficiently removing corrupted and empty photos before compressing the data onto Amazon S3 before migrating the data on MongoDB. Finally, we used EC2 to connect to the Amazon S3-MongoDB database infrastructure. 

## Issues with the data and their solutions:

-Bad images: filter out obvious images by their size using glob and os

-Pixels: RGB photos have a different pixel dimension than B/G (specifically 128x128x3 vs 128x128 respectively). Our solution was the convert all images to black and white. 

-Different sized images: resize all images to match a certain size for logistic regression 
