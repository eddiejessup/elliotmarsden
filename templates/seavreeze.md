## [Seavreeze](https://github.com/eddiejessup/cv)

I think the way I make my <small>CV</small> is useful enough for me to be of general interest. I like to customize its contents for each job application, which was initially a pain, because I had to fiddle with the LaTeX source to show or hide different bits of content depending on their relevance for the job. I also maintained two versions, one for this website and one to make a pretty <small>PDF</small>, which was frustrating. <small>CV</small>s have a pretty consistent structure, so I tried to solve my problem by maintaining one <small>YAML</small> file in which the actual contents live, and then rendering <small>HTML</small> and LaTeX files from these. The <small>HTML</small> went on this website, the second to a <small>PDF</small>.

For example, the input <small>YAML</small> file might look like this (contents are hypothetical):

```yaml
name: 'Illir Muzden'
date_of_birth: '1989-03-28'
address:
    street: 'Surferstreet 11/1'
    city: 'Amsterdam'
    postcode: '1777 AS'
    country: Netherlands
email: 'illir.muzden@gmail.com'
phone: '+31 65553944'
website: 'illirmuzden.com'
github_name: 'adderbuzzup'
summary: ''
jobs:
    -
        date: 'May 2016 – Present'
        employer: 'Looking.ca'
        role: 'Data Scientist'
        summary: 'Analysis of large data-sets to identify trends to allow appropriate business decisions.'
        points:
            - 'Querying petabyte-scale data using Hadoop and related tools such as Hive and Spark to answer business questions.'
            - ...
```

I wrote a program that substituted these values as the context of LaTeX and <small>HTML</small> Jinja2 templates.

This worked for simple content, but I wanted finer control over the output. For example, say I wanted to tell the world that I've used the NoS<small>QL</small> database "MongoDB". This sort of string confuses TeX's hyphenation logic, so it has no problem breaking a line like this:

```plaintext
I'm super duper amazing at using Mon-
goDB, trust me mate, and also at loads
of other NoSQL things as well yeeaah.
```

which looks horrible. If I were only targeting TeX, I could fix this by preventing hyphenation of the word: `\hbox{MongoDB}` (let's not get into what this is doing, this is not the place). But how should I tell the <small>HTML</small> renderer what to do with this? I can't have bare TeX commands being passed through to the <small>HTML</small> version.

Because of issues like these, I ended up maintaining two <small>YAML</small> files, one for the HTML and one for the TeX. This let me include all of the markup I wanted, and it let me toggle on or off different sections more easily than in the TeX, but I still had to keep the two versions in sync.

In order to be able to crack this walnut-sized problem, I made a sledging hammer in the form of a little <small>XML</small>-based markup language, which I call <small>'CVML'</small>. One might wonder, given that I was *already* writing my <small>CV</small> in a markup language, <small>YAML</small>, why I wouldn't just use *its* structure to specify what I want. I got myself confused wondering why this wouldn't work, until I realized that <small>YAML</small> isn't *really* a markup language; one can't easily use it to mark up continuous text. Indeed, I discovered that <small>YAML</small> doesn't stand for 'Yet Another Markup Language', as I had presumed, but '<small>YAML</small> Ain't Markup Language'.

Anyway, so I stuck with <small>YAML</small> for specifying the elements in my <small>CV</small>, but allowed <small>CVML</small> in the strings, to mark up the text with presentational details. The simplest <small>CVML</small> tag, `[[mu]]` (for MarkUp), looks like this:

```xml
I'm super duper amazing at using
[[mu]][[tex]]\hbox{MongoDB}[[/tex]][[html]]MongoDB[[/html]][[/mu]],
trust me mate, and also at loads of
other NoSQL things as well yeeaah.
```

It sure has the verbosity of <small>XML</small>, but I don't know of a better alternative. A `[[mu]]` tag has children that specify the content to show for each language to be rendered. At render-time, the tag expands to the appropriate section of text. One snag was that, because this section might be a snippet of <small>HTML</small>, and <small>CVML</small> is <small>XML</small>-based, I faced the terror of having to escape all of the angle brackets in the <small>HTML</small> content, so that it wouldn't be mistaken for part of the <small>CVML</small>. I solved this by using characters other than angle brackets for <small>CVML</small>, as you can see, and substituting the characters for angle brackets just before parsing the tag. Between TeX and <small>HTML</small>, most of the good delimiters are taken, so I went with a multi-character delimiter.

Anyway, so I realized that with this tag I could go crazy with markup. I have the unfortunate combination:

- I want to solve problems that require tools whose names tend to involve acronyms and initialisms
- I am distracted by strings of uppercase characters in continuous text

The first means that I feel compelled to boast that I've used various tools whose names are constituted of an unusually high share of characters from the upper case. When combined with the second, I'm at risk of hating the sight of my own life on paper. I avoid this through excesses of <small>SMALL CAPS</small> styling, which maintains semantic and legal correctness, while looking less shouty. Anyway, I started modifying my <small>CV</small> data like so:

```xml
I'm super duper amazing at using
[[mu]][[tex]]\hbox{MongoDB}[[/tex]][[html]]MongoDB[[/html]][[/mu]],
trust me mate, and also at loads of other
NoS[[mu]][[tex]]\smaller{QL}[[/tex]][[html]]<small>QL</small>[[/html]][[/mu]]
things as well yeeaah.
```

(`\smaller` is a user-defined TeX macro, and `<small>` is an <small>HTML</small> tag. Don't worry, it sounds presentational but somehow it counts as semantic, so it's allowed in <small>HTML5</small>.)

I realized this was becoming ugly, so I added a `[[small]][text][[/small]]` <short>CVML</short> tag, which generates the correct markup internally, depending on the language:

```xml
I'm super duper amazing at using
[[mu]][[tex]]\hbox{MongoDB}[[/tex]][[html]]MongoDB[[/html]][[/mu]],
trust me mate, and also at loads of other
NoS[[small]]QL[[/small]] things as well yeeaah.
```

I've now added the same sort of tags to emphasise text (`[[cite]]<text>[[/cite]]`) and generate links (`[[link]][[url]]<url>[[/url]][[name]]<name>[[/name]][[/link]]`).

The result of this work is that I now only have one file to maintain, instead of two. Just one file, a markup language, and a multi-step document preparation pipeline...
