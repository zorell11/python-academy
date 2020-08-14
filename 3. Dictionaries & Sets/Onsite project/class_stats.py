classes = {'Biology' : ['Adam','Chelsea','Marcus','Oliver','Alex','Sandra','Ann'],
            'Math' : ['Marcus','Alex','Glenn','Samuel','Clara','Chelsea'],
            'PE'  : ['Adam','Tyler', 'Alex','Clara'],
            'Social Sciences': ['Abraham','Marcus','Alex','Glenn','Clara'],
            'Chemistry' : ['Alfred', 'Curt','Oliver','Alex','Tyler','Ann']}


stats =  set(classes['Biology']) & set(classes['PE']) & set(classes['Math']) & set(classes['Social Sciences']) & set(classes['Chemistry'])
print("Students inscribed into all the subjects:",stats)
