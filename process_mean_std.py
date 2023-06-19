import pandas as pd

def process_mean_std(tsv):

    # Import data
    data = pd.read_csv(tsv, sep='\t', encoding='utf-8')
    
    # Rename columns
    df = data.rename(columns={
        'Result': 'res',
        'Row':'row',
        'Column': 'col',
        'Well': 'well',
        'Nuclei - Number of Objects': 'n_nuc',
        'Nuclei - Nucleus Area [µm²] - Mean per Well': 'area_mean',
        'Nuclei - Nucleus Area [µm²] - StdDev per Well': 'area_std',
        'Number of Analyzed Fields': 'n_fields'
        })
    print(df.columns)
    # Add days column
    days = df.res.str.split(pat=' > ', expand=True)[0].str[-1].rename('day')
    df = pd.concat([days, df], axis = 1)

    # Sort values
    df = df.sort_values(['cell_name', 'cell_number', 'day'])

    # Create final DF
    n1 = 4 * df.cell_number.unique().shape[0]
    final = df.loc[::n1, ['cell_name', 'day']].sort_values(by=['cell_name', 'day'])
    a = pd.DataFrame() 
    for cell_name in df.cell_name.unique():
        for day in df.day.unique():
            b = df.loc[(df.day == day) & (df.cell_name == cell_name), ['area_mean', 'area_std']].transpose()
            b.columns = [f'{num}_{i+1}' for num in df.cell_number.unique() for i in range(4) ]
            a = pd.concat([a, b], axis=0, ignore_index=True)
    final = final.loc[final.index.repeat(2)]
    final.index = a.index
    legend =pd.DataFrame({'area_measure': ['mean', 'std'] * (len(a) // 2)})
    demo = pd.concat([final, legend, a], axis = 1)
    demo
    return demo

