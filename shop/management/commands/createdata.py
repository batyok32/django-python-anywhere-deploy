from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from shop.models import Category, Product, Subcategory, Brand, Comment
from django.conf import settings
from authentication.models import UserAccount

class Provider():
    
    def ecommerce_category(self, col, fake, swrite, style):
        swrite.write(style.SUCCESS("\nSTARTED GENERATING CATEGORIES\n"))
        for i in range(int(col)):
            i+=1
            text= fake['en_US'].text(max_nb_chars=6)
            swrite.write(style.WARNING(f"\n{i}. Start creating"))
            print(f">> '{text}'")
            slug = slugify(text)
            category = Category.objects.language('en').create(name=f"en- {text}", slug=slug)
            
            category.set_current_language('tk')
            text = fake['en_US'].text(max_nb_chars=6)
            category.name=f"tk- {text}"

            category.set_current_language('ru')
            text = fake['ru_RU'].text(max_nb_chars=6)
            category.name=f"ru- {text}"

            category.save()
            swrite.write(style.SUCCESS(f"\n{i}. Created"))
            print(f">> '{text}'" )
        check_categories = Category.objects.all().count()
        swrite.write(style.SUCCESS(f"\nNumber of categories: {check_categories}"))
    
    def ecommerce_comments(self, col, pro_id, fake, swrite, style):
        product = Product.objects.get(id=pro_id)
        user =  UserAccount.objects.first()
        swrite.write(style.SUCCESS("\nSTARTED GENERATING COMMENTS\n"))
        
        for i in range(int(col)):
            i+=1
            text= fake.text(max_nb_chars=200)
            swrite.write(style.WARNING(f"\n{i}. Start creating"))
            print(f">> '{text}'")
            Comment.objects.create(body=text, product=product, user=user)
            swrite.write(style.SUCCESS(f"\n{i}. Created"))
            print(f">> '{text}'" )
        check_comments = Comment.objects.filter(product=product).count()
        swrite.write(style.SUCCESS(f"\nNumber of comments for this '{product.name}' product: {check_comments}"))

    def ecommerce_subcategory(self, col, fake, cat_id, swrite, style):
        category = Category.objects.get(id=cat_id)
        swrite.write(style.SUCCESS("\nSTARTED GENERATING SUBCATEGORIES\n"))
        for i in range(int(col)):
            i+=1
            text = fake['en_US'].text(max_nb_chars=20)
            swrite.write(style.WARNING(f"\n{i}. Start creating"))
            print(f">> '{text}'")
            slug = slugify(text)
            subcategory = Subcategory.objects.language('en').create(name=f"en- {text}", slug=slug, category=category)
            
            subcategory.set_current_language('tk')
            text = fake['en_US'].text(max_nb_chars=20)
            subcategory.name=f"tk- {text}"

            subcategory.set_current_language('ru')
            text = fake['ru_RU'].text(max_nb_chars=20)
            subcategory.name=f"ru- {text}"

            subcategory.save()

            swrite.write(style.SUCCESS(f"\n{i}. Created"))
            print(f">> '{text}'" )
        check_subcategories = Subcategory.objects.filter(category=category).count()
        swrite.write(style.SUCCESS(f"\nNumber of subcategories: {check_subcategories}"))

    def ecommerce_brands(self, col, fake, cat_id, swrite, style):
        category = Category.objects.get(id=cat_id)
        swrite.write(style.SUCCESS("\nSTARTED GENERATING BRANDS\n"))
        for i in range(int(col)):
            i+=1
            text = fake['en_US'].text(max_nb_chars=20)
            swrite.write(style.WARNING(f"\n{i}. Start creating"))
            print(f">> '{text}'")
            slug = slugify(text)
            brand = Brand.objects.language('en').create(name=f"en- {text}", slug=slug, category=category)
            
            brand.set_current_language('tk')
            text = fake['en_US'].text(max_nb_chars=20)
            brand.name=f"tk- {text}"
            brand.slug=slug

            brand.set_current_language('ru')
            text = fake['ru_RU'].text(max_nb_chars=20 )
            brand.name=f"ru- {text}"
            brand.slug=slug

            brand.save()

            swrite.write(style.SUCCESS(f"\n{i}. Created"))
            print(f">> '{text}'" )
        check_brands = Brand.objects.filter(category=category).count()
        swrite.write(style.SUCCESS(f"\nNumber of brands: {check_brands}"))
        

    def ecommerce_products(self, col, fake, swrite, style, cat_id, sub_id, brand_id):
        subcategory = Subcategory.objects.get(id=sub_id)
        categor= Category.objects.get(id=cat_id)
        brand = Brand.objects.get(id=brand_id)
        swrite.write(style.SUCCESS("\nSTARTED GENERATING PRODUCTS\n"))
        for i in range(int(col)):
            i+=1
            text = fake['en_US'].text(max_nb_chars=20)
            swrite.write(style.WARNING(f"\n{i}. Start creating"))
            print(f">> '{text}'")
            slug = slugify(text)
            desc = fake.text(max_nb_chars=2000)
            price = fake.random_int(min=10, max=1000)
            amount = fake.random_int(min=10, max=100)
            
            product = Product.objects.language('en').create(name=f"en- {text}", slug=slug, description=desc, category=categor, subcategory=subcategory, price=price, brand=brand, amount=amount)
            
            product.set_current_language('tk')
            text = fake['en_US'].text(max_nb_chars=20)
            product.name=f"tk- {text}"
            product.description=desc

            product.set_current_language('ru')
            text = fake['ru_RU'].text(max_nb_chars=20)
            product.name=f"ru- {text}"
            product.description=desc

            product.save()
            swrite.write(style.SUCCESS(f"\n{i}. Created"))
            print(f">> '{text}'" )
        check_products = Product.objects.all().count()
        swrite.write(style.SUCCESS(f"\nNumber of products: {check_products}"))
        
        

# calm

class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):
        fake = Faker(['en_US', 'ru_RU'])
        # fake.add_provider(Provider)
        swrite = self.stdout
        style=self.style
        
        while True:
            select = input("""
==============================================
=                      Hello!
= What do you want to generate >
= 1. Products
= 2. Categories
= 3. Subcategories
= 4. Brands
= 5. Comments
= (choose a number)
==============================================
            """)
            if int(select) == 1:
                col_products = input("How many products do you want to generate >>>")
                cat_id = input("For which category >>>")
                brand_id = input("For which brand >>>")
                sub_id = input("For which subcategory >>>")
                if col_products.isnumeric() and cat_id.isnumeric() and brand_id.isnumeric() and sub_id.isnumeric():
                    Provider.ecommerce_products(self,col=col_products, fake=fake, swrite=swrite, style=style, cat_id=cat_id, sub_id=sub_id, brand_id=brand_id)
                    
                else:
                    self.stdout.write(self.style.ERROR("Not correct"))

            elif int(select) == 2:
                col_categories = input("How many categories do you want to generate >>>")
                
                if col_categories.isnumeric():
                    Provider.ecommerce_category(self, col=col_categories, fake=fake, swrite=swrite, style=style)
                    
                else:
                    self.stdout.write(self.style.ERROR("Not correct"))

            elif int(select) == 3:
                col_subcategories = input("How many subcategories do you want to generate >>>")
                cat_id = input("For which category do you want to generate subcategories >>>")
                
                if col_subcategories.isnumeric() and cat_id.isnumeric():
                    Provider.ecommerce_subcategory(self, col=col_subcategories,cat_id=cat_id, fake=fake, swrite=swrite, style=style)

                else:
                    self.stdout.write(self.style.ERROR("Not correct"))
            elif int(select) == 4:
                col_brands = input("How many brands do you want to generate >>>")
                cat_id = input("For which category do you want to generate brands >>>")
                
                if col_brands.isnumeric() and cat_id.isnumeric():
                    Provider.ecommerce_brands(self, col=col_brands, cat_id=cat_id, fake=fake, swrite=swrite, style=style)
                else:
                    self.stdout.write(self.style.ERROR("Not correct"))
            elif int(select) == 5:
                col_comments = input("How many comments do you want to generate >>>")
                pro_id = input("For which product do you want to generate >>>")
                
                if col_comments.isnumeric() and pro_id.isnumeric():
                    Provider.ecommerce_comments(self, col=col_comments, pro_id=pro_id, fake=fake, swrite=swrite, style=style)
                else:
                    self.stdout.write(self.style.ERROR("Not correct"))
            else:
                print("Bye")
                break
                
        

   
   
  
   
    
   