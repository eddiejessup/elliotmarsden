# Book list

I like the idea of a decentralized network of shareable objects. All that is needed is two things, to be able to generate a searchable network:

- A list of which objects I own
- The locations of the lists of people I know

My usual example of this network is that of books. Books are an incredibly under-exploited resource: they are free to use, and are unused for essentially all of their existence. Printing new copies of old books is a terrible waste. If we can find a way to get books to people who want to read them, we can stop printing new copies of Dickens. If the edges of the network represent social relationships, we might be able to make new friends at the same time.

So, my proposal is to all make a file of the following format:

    [books]
    - author_1: title_1
    - author_2: title_2
    ...
    - author_n: title_n

    [people]
    - friend_1_website.com/book_list
    - google.docs.com/friend_2/book_list
    ...
    - friendm.dropbox.com/misc/book_list

And make it available at some publicly accessible address. From there, it's trivial for anyone to build a spider to search from your own point, to the closest social neighbor who has the book you want.

To get started, [here](https://gist.githubusercontent.com/eddiejessup/6fb19be7bb4b3f969fa943341af78919/raw/76fb36bde8f2ab424ad08a77d01d046882869073/book_list) is my book list. Sorry it's short, I just wanted to get the proof of concept down.

<script src="https://gist.github.com/eddiejessup/6fb19be7bb4b3f969fa943341af78919.js"></script>
