`Subject:` Pandas
<br />`Date:` 12 Oct 22 `No.` 20

### Tasks:
1. Load scraping data from this [task](https://github.com/AhmedUKamel/INSTANT-AI/blob/main/Mini%20Project%202/INSTANT%20Mini%20Project%202.pdf) to `DataFrame` | [Solution](https://github.com/AhmedUKamel/INSTANT-AI/blob/main/Mini%20Project%202/Scrape-top-250-movie.ipynb)

### Notes:
* Cannot append `dictionary` to `DataFrame` with ignore_index=False
~~~python
df.append(
    {
        'Name':'Ahmed',
        'Age':20
    },
    ignore_index=False
)
~~~
    Output:
    TypeError: Can only append a dict if ignore_index=True

**Solution**
~~~python
df.append(
    pd.DataFrame({
        'Name' : 'Added',
        'Age'  : 25
    }, 
    index=['Fourth']),
    ignore_index=False,
)
~~~
* `df.loc` slices by applied index, while `df.iloc` slices by numerical index.