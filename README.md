# faber-challenge-2017

Repository to work on Faber Ventures Challenge 2017 - Amazon Movie Recommendation Engine


Given the database available at http://snap.stanford.edu/data/web-Movies.html create a recommendation engine
With a user id that outputs the recommend movies for said user

The project is not finished. My aim was to scrap the webpages of the given movies (needed to spoof the acess to URLs as a workaround to the Amazon anti-bot system).

Given the reviews with a good ratio of helpfullness I was going to construct a model that was able to the following

1) User buys A-B-C
2) Another user has bought A-B-C-D
3) Recommend D

#### OR

1) User buys A
2) Check the genre of A
3) Recommend the best reviewed in that genre

- [x] Web Scrapped info
- [x] Started to look at it, define helpfullness
- [ ] Finished the recommendation
