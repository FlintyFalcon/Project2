from django.db import models

## Describes all about our business, location, contact info, and directions to get there.
class About(models.Model):
    title = models.CharField(max_length = 30)

## Describes all the movies that are currently playing, showtimes, link to buy tickets, and has thumbnail
class Movies(models.Model):
    title = models.CharField(max_length = 30)

## More detail on a specific movie. Synopsis, ratings, and cast
class Synopsis(models.Model):
    title = models.CharField(max_length = 30)

## Storefront to sell merch for our business. Shirts, mugs, stickers, gift cards.
class Store(models.Model):
    title = models.CharField(max_length = 30)