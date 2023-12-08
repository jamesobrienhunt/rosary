# JMJ

hail_mary = "Hail, Mary, full of grace, the Lord is with thee. Blessed art thou amongst women and blessed is the fruit of thy woumb, Jesus. Holy Mary, Mother of God, pray for us sinners, now and at the hour of our death. Amen."


print(hail_mary[0:hail_mary.find('the Lord is with thee.')])
print(hail_mary[hail_mary.find('the Lord is with thee.'):hail_mary.find(' Blessed art thou amongst women')])
print(hail_mary[hail_mary.find('Blessed art thou amongst women'):hail_mary.find(' and blessed is the fruit of thy woumb, Jesus.')])
print(hail_mary[hail_mary.find('and blessed is the fruit of thy woumb, Jesus.'):hail_mary.find(' Holy Mary, Mother of God,')])
print(hail_mary[hail_mary.find('Holy Mary, Mother of God,'):hail_mary.find(' pray for us sinners,')])
print(hail_mary[hail_mary.find('pray for us sinners,'):hail_mary.find(' now and at the hour of our death.')])
print(hail_mary[hail_mary.find('now and at the hour of our death.'):hail_mary.find(' Amen.')])
print(f"\n{hail_mary[hail_mary.find('Amen.'):]}")