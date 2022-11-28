Collected Knowledge & Wisdom on
# Animechan
Provides Anime Quotes
https://github.com/rocktimsaikia/anime-chan
---
## Provides:
This API provides the following get the following:
  - A random quote (https://animechan.vercel.app/api/random)
  - A random quote by title (https://animechan.vercel.app/api/random/anime?title=[insert title])
  - A random quote by character (https://animechan.vercel.app/api/random/character?name=[insert name])
  - 10 random quotes (https://animechan.vercel.app/api/quotes)
  - 10 quotes by title (https://animechan.vercel.app/api/quotes/anime?title=[insert title])
  - 10 quotes by character (https://animechan.vercel.app/api/quotes/character?name=[insert name])
- Pagination (only for query endpoints)

### Pain factor: 2

### Key Provisioning:     
- This is different from NASA in the sense that you don’t need a personal key in order to access the information. All of the provided information is either static (in the case of generating quotes by character or title) or randomly provided from what I’d assume is a static database.

### Quotas:
- 100 requests per hour (I’m guessing this number is much lower than NASA’s because it is casually served by a single individual)

### Notes:
- When inputting queries for shows or characters with multiple available titles, default to the most common one or, in the case of show titles, the English title.

---

## The Good:
- Good documentation
- Easy to use
- No need for a personal key
- Entertaining
- Weird capitalization doesn’t appear to be an issue. https://animechan.vercel.app/api/quotes/anime?title=GINTAMA returns the same results as https://animechan.vercel.app/api/quotes/anime?title=gintama, which is convenient.

## The Bad:
- What I see as the largest problem and the root of many other listed issues: Currently no available list of characters or anime, so there isn’t a way to see if the problem is that the anime isn’t available or if you’re typing it in incorrectly.
- The queries are not very advanced, so it seems like the way it fetches data is by matching the query with any title or name in the database that contains the query. This means that when submitting a request, you will often be given excess data that doesn’t actually match your request.
  - For example, you can submit the request ```https://animechan.vercel.app/api/quotes/anime?title=o``` and will be given a list of quotes from anime with titles that contain the character “o”.
  You can imagine what would happen if you wanted quotes from a specific show with short titles or with series that have repeating titles.
  - Ex 1: There is a show called “K”, but if you were to submit that as your query string, you would be given a series of quotes from other shows such as “Hyouka” instead. In this case, you would need to go for the alternate title of “K Project” to retrieve appropriate results.
  - Ex 2: Gintama is a show with many sequels, most of which contain “Gintama” in their titles. This means that if you submit a query for the original “Gintama”, you’ll be given a bunch of results from the sequels such as “Gekijōban Gintama Kanketsu-hen: Yorozuya yo Eien Nare”.
- The maximum number of quotes available for each title isn’t the same for all queries. This means that when utilizing pagination, you won’t know whether the page you requested will return data or a ```{"error":"No quotes found!"}``` page.
- Only options are 1 or 10 quotes at a time. Creator mentioned changing this in the future.

## The Ugly:
- Not necessarily bad, but when you want to ask for an anime with spaces in the name, you would just type the title in with the spaces in the url. This means that the link isn’t “slugified” and can be difficult to work with.
  - You can replace spaces with + or %20 in the url.
- It’s difficult to deal with all the weird things anime titles do. Take special characters as an example:
  - You get different results if you type in your title query for 10 quotes as “Steins;gate” and “Steins gate” which is weird. These should be the same show, but you get two valid and different results for both requests. The first one gives results with the title as “Steins;Gate” and the second with “Steins Gate”.

**Location of documentation:** https://animechan.vercel.app/

---

Accurate as of (last update):    2022-11-27

Contributors:
Julia Lee, pd 2
