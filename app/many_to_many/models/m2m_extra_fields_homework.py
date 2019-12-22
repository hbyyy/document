from django.db import models


#
# class Customer(models.Model):
#     email = models.EmailField(max_length=20)
#     name = models.CharField(max_length=20)
#     address = models.CharField(max_length=50)
#
#     def __str__(self):
#         return '{email}, {name}'.format(email=self.email, name=self.name)
#
#
# class Shop(models.Model):
#     name = models.CharField(max_length=20)
#     customers = models.ManyToManyField(Customer, through='Shipping')
#
#     def __str__(self):
#         return self.name
#
#
# class Item(models.Model):
#     name = models.CharField(max_length=20)
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Shipping(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
#     start_date = models.DateTimeField(null=True)
#     end_date = models.DateTimeField(null=True)
#
#     def __str__(self):
#         return '샵: {shop} ,  고객 : {customer}, 배송출발 : {start_date}, 배송완료 : {end_date}'.format(
#             shop=self.shop,
#             customer=self.customer,
#             start_date=self.start_date if self.start_date else '배송준비중',
#             end_date=self.end_date if self.end_date else ' '
#         )


class Writer(models.Model):
    name = models.CharField(max_length=20)
    platforms = models.ManyToManyField('Platform', through='Webtoon')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'm2m_writer'


class Platform(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'm2m_platform'


class Webtoon(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'' \
               f'({self.writer}, {self.platform}) , {self.title}'

    class Meta:
        db_table = 'm2m_webtoon'
