from staticjinja import make_site


if __name__ == "__main__":
    site = make_site(
        outpath='public',
        staticpaths=['static/'],
    )
    site.render(use_reloader=False)
