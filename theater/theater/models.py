from django.db import models

## Describes all about our business, location, contact info, and directions to get there.
class About(models.Model):
    business = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    contact = models.CharField(max_length=12)
    ##Assuming Contact is used for phone numbers

## Describes all the movies that are currently playing, showtimes, link to buy tickets, and has thumbnail
class Movies(models.Model):
    title = models.CharField(max_length=50)
    showtime = models.CharField(max_length=15)
    ## Example showtime = "Jan. 15 1045 PM"
    ##Link needs to be added
    thumbnail = models.ImageField()
    ## A height.field and width.field attributes can be added


## More detail on a specific movie. Synopsis, ratings, and cast
class Synopsis(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField()
    ratings = models.CharField(max_length=4)
    ## Example: 1/10, 8/10.
    cast = models.CharField(max_length=125)
    ##Names of cast members


## Storefront to sell merch for our business. Shirts, mugs, stickers, gift cards.
class Store(models.Model):
    title = models.CharField(max_length=150)
	