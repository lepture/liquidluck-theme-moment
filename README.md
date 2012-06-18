# Moment Theme for Felix Felicis

## Installation

Place it in your blog:

```
your_blog/
    settings.py
    content/
    _themes/
        moment/
```

You can use git submodule for convience:

```
$ git submodule add git://github.com/lepture/liquidluck-theme-moment.git _themes/moment
```

## Configuration

Edit your settings.py, change your theme to:

```python
theme = 'moment'
```


## Customize

You can customize your theme with ``theme_variables``.

+ Change Navigation (example)

```python
theme_variables = {
    'navigation': [
        ('Home', '/'),
        ('Life', '/life/'),
        ('Work', '/work/'),
    ],
}
```

+ Google Analytics

```python
theme_variables = {
    'analytics': 'UA-xxxx',
}
```

+ Disqus Comment Support

```python
theme_variables = {
    'disqus': 'your-disqus-shortname',
}
```

All in one:

```
theme_variables = {
    'navigation': [
        ('Home', '/'),
        ('Life', '/life/'),
        ('Work', '/work/'),
    ],
    'analytics': 'UA-xxxx',
    'disqus': 'your-disqus-shortname',
}
```
