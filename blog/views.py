from django.shortcuts import render
from datetime import date
# Create your views here.
posts = [
    {
        "slug":"berthoud",
        "image":"theSisters.jpeg",
        "author":"Nick",
        "date": date(2022,1,14),
        "title":"Berthoud, Co",
        "excerpt":"Amazing views of Longs Peak and Mt. Meeker",
        "content" : """
            Vero numquam rerum architecto, perspiciatis placeat sit quibusdam harum nemo molestias velit aliquam dolorem ad, 
            qui quibusdam optio quaerat, hic reiciendis laudantium natus sit illo ut quisquam suscipit, 
            sunt libero labore assumenda nostrum nam ipsam ad commodi autem? Mollitia corrupti harum ipsam aliquid eveniet reprehenderit saepe. 
            Facere ipsum placeat consequuntur quisquam harum sed at? Est a laborum cumque fugiat inventore ipsum animi repellat quod quae voluptatibus, 
            quasi magni beatae repellendus? Reprehenderit alias exercitationem possimus, quisquam ullam quis vel possimus beatae voluptas perspiciatis, 
            error ab qui, omnis expedita id odit quo hic obcaecati incidunt nostrum dignissimos soluta aliquam. Neque placeat cumque hic sed totam mollitia, 
            obcaecati eum blanditiis porro corporis autem in, aperiam deleniti quia natus quidem, totam dolorum molestiae suscipit maiores quisquam porro tempore
            vitae corporis fugit nobis.

            Nesciunt saepe necessitatibus laborum modi ipsum quasi officia. Molestias totam pariatur, alias consequatur molestiae ratione ab quasi,
            odit est saepe officiis porro velit eos id doloremque laudantium odio, neque animi commodi corporis minus dolorum accusamus at ut quam?
            Ipsam at impedit animi, vero unde rem facilis error amet sint asperiores atque, at non recusandae blanditiis repellat voluptate harum cum eos in,
            laboriosam voluptatum nisi perspiciatis, suscipit laboriosam cumque est dolor doloribus? Nulla expedita numquam alias quo perferendis hic veniam 
            optio, sint modi est laborum nemo saepe dignissimos fugit ea? Rem doloribus omnis similique id commodi nostrum veritatis labore excepturi quis 
            perspiciatis, modi nesciunt porro harum obcaecati ut saepe itaque provident sequi. Aut alias nostrum, enim velit odit ducimus, culpa assumenda 
            consequatur, dolores dignissimos illum soluta ducimus voluptatum culpa non quia ipsam similique maiores? Veniam iusto rem et recusandae cum 
            molestiae assumenda, amet at placeat laboriosam vero incidunt doloribus, dolor perspiciatis ducimus possimus enim molestiae neque fuga. 
            Rem ratione odit maxime sit mollitia. Saepe hic quisquam enim ea animi magni provident fuga sint, dicta maxime tempore hic beatae molestias 
            deleniti. Praesentium magnam dignissimos quae, expedita magnam repellendus itaque totam similique optio.

            Voluptates magnam magni quos nam minima mollitia, beatae dolor reiciendis quo explicabo a animi soluta ipsam architecto illo rem, 
            cumque delectus voluptatem est ducimus corrupti minus iste quos beatae voluptate, sit maxime eos explicabo porro fugit officia hic, 
            quas officia consequuntur eaque aut fuga animi architecto tempora. Officia voluptatum voluptatibus nemo ipsam qui nostrum dignissimos 
            libero perspiciatis? Natus harum repudiandae veniam doloremque eveniet, nemo quibusdam ipsam, inventore delectus commodi odio ipsa, 
            eligendi possimus earum officiis amet? Omnis voluptatibus harum quae ullam consequatur veniam rerum, debitis aut maxime cupiditate? 
            Unde aperiam incidunt quia, dolorum et earum ea culpa ut, nostrum minima saepe quasi nulla veritatis deserunt nemo, labore unde in 
            possimus numquam sapiente. Expedita recusandae repudiandae quos voluptatum mollitia consequatur doloribus fugit dolorem quisquam laboriosam, 
            laboriosam quisquam sunt nulla quibusdam in, suscipit dicta iusto aspernatur expedita eveniet accusantium illum quam corporis natus facilis, 
            reiciendis quo ab unde optio consequuntur quis fugit fugiat. Temporibus voluptatum dicta impedit adipisci officia aperiam deleniti nostrum quibusdam? 
            Adipisci ut veniam necessitatibus optio unde officia quia expedita, consequatur aliquam doloremque corrupti?
        """
    },
    {
        "slug":"horsetooth",
        "image":"horsetooth.jpeg",
        "author":"Nick",
        "date": date(2023,2,15),
        "title":"Horse Tooth Resevour",
        "excerpt":"the best place to hike to swim in CO",
        "content" : """
            Vero numquam rerum architecto, perspiciatis placeat sit quibusdam harum nemo molestias velit aliquam dolorem ad, 
            qui quibusdam optio quaerat, hic reiciendis laudantium natus sit illo ut quisquam suscipit, 
            sunt libero labore assumenda nostrum nam ipsam ad commodi autem? Mollitia corrupti harum ipsam aliquid eveniet reprehenderit saepe. 
            Facere ipsum placeat consequuntur quisquam harum sed at? Est a laborum cumque fugiat inventore ipsum animi repellat quod quae voluptatibus, 
            quasi magni beatae repellendus? Reprehenderit alias exercitationem possimus, quisquam ullam quis vel possimus beatae voluptas perspiciatis, 
            error ab qui, omnis expedita id odit quo hic obcaecati incidunt nostrum dignissimos soluta aliquam. Neque placeat cumque hic sed totam mollitia, 
            obcaecati eum blanditiis porro corporis autem in, aperiam deleniti quia natus quidem, totam dolorum molestiae suscipit maiores quisquam porro tempore
            vitae corporis fugit nobis.

            Nesciunt saepe necessitatibus laborum modi ipsum quasi officia. Molestias totam pariatur, alias consequatur molestiae ratione ab quasi,
            odit est saepe officiis porro velit eos id doloremque laudantium odio, neque animi commodi corporis minus dolorum accusamus at ut quam?
            Ipsam at impedit animi, vero unde rem facilis error amet sint asperiores atque, at non recusandae blanditiis repellat voluptate harum cum eos in,
            laboriosam voluptatum nisi perspiciatis, suscipit laboriosam cumque est dolor doloribus? Nulla expedita numquam alias quo perferendis hic veniam 
            optio, sint modi est laborum nemo saepe dignissimos fugit ea? Rem doloribus omnis similique id commodi nostrum veritatis labore excepturi quis 
            perspiciatis, modi nesciunt porro harum obcaecati ut saepe itaque provident sequi. Aut alias nostrum, enim velit odit ducimus, culpa assumenda 
            consequatur, dolores dignissimos illum soluta ducimus voluptatum culpa non quia ipsam similique maiores? Veniam iusto rem et recusandae cum 
            molestiae assumenda, amet at placeat laboriosam vero incidunt doloribus, dolor perspiciatis ducimus possimus enim molestiae neque fuga. 
            Rem ratione odit maxime sit mollitia. Saepe hic quisquam enim ea animi magni provident fuga sint, dicta maxime tempore hic beatae molestias 
            deleniti. Praesentium magnam dignissimos quae, expedita magnam repellendus itaque totam similique optio.

            Voluptates magnam magni quos nam minima mollitia, beatae dolor reiciendis quo explicabo a animi soluta ipsam architecto illo rem, 
            cumque delectus voluptatem est ducimus corrupti minus iste quos beatae voluptate, sit maxime eos explicabo porro fugit officia hic, 
            quas officia consequuntur eaque aut fuga animi architecto tempora. Officia voluptatum voluptatibus nemo ipsam qui nostrum dignissimos 
            libero perspiciatis? Natus harum repudiandae veniam doloremque eveniet, nemo quibusdam ipsam, inventore delectus commodi odio ipsa, 
            eligendi possimus earum officiis amet? Omnis voluptatibus harum quae ullam consequatur veniam rerum, debitis aut maxime cupiditate? 
            Unde aperiam incidunt quia, dolorum et earum ea culpa ut, nostrum minima saepe quasi nulla veritatis deserunt nemo, labore unde in 
            possimus numquam sapiente. Expedita recusandae repudiandae quos voluptatum mollitia consequatur doloribus fugit dolorem quisquam laboriosam, 
            laboriosam quisquam sunt nulla quibusdam in, suscipit dicta iusto aspernatur expedita eveniet accusantium illum quam corporis natus facilis, 
            reiciendis quo ab unde optio consequuntur quis fugit fugiat. Temporibus voluptatum dicta impedit adipisci officia aperiam deleniti nostrum quibusdam? 
            Adipisci ut veniam necessitatibus optio unde officia quia expedita, consequatur aliquam doloremque corrupti?
        """
    },
    {
        "slug":"hanging-lake",
        "image":"hangingLake.jpeg",
        "author":"Nick",
        "date": date(2022,2,14),
        "title":"Hanging Lake",
        "excerpt":"One mile straight up",
        "content" : """
            Vero numquam rerum architecto, perspiciatis placeat sit quibusdam harum nemo molestias velit aliquam dolorem ad, 
            qui quibusdam optio quaerat, hic reiciendis laudantium natus sit illo ut quisquam suscipit, 
            sunt libero labore assumenda nostrum nam ipsam ad commodi autem? Mollitia corrupti harum ipsam aliquid eveniet reprehenderit saepe. 
            Facere ipsum placeat consequuntur quisquam harum sed at? Est a laborum cumque fugiat inventore ipsum animi repellat quod quae voluptatibus, 
            quasi magni beatae repellendus? Reprehenderit alias exercitationem possimus, quisquam ullam quis vel possimus beatae voluptas perspiciatis, 
            error ab qui, omnis expedita id odit quo hic obcaecati incidunt nostrum dignissimos soluta aliquam. Neque placeat cumque hic sed totam mollitia, 
            obcaecati eum blanditiis porro corporis autem in, aperiam deleniti quia natus quidem, totam dolorum molestiae suscipit maiores quisquam porro tempore
            vitae corporis fugit nobis.

            Nesciunt saepe necessitatibus laborum modi ipsum quasi officia. Molestias totam pariatur, alias consequatur molestiae ratione ab quasi,
            odit est saepe officiis porro velit eos id doloremque laudantium odio, neque animi commodi corporis minus dolorum accusamus at ut quam?
            Ipsam at impedit animi, vero unde rem facilis error amet sint asperiores atque, at non recusandae blanditiis repellat voluptate harum cum eos in,
            laboriosam voluptatum nisi perspiciatis, suscipit laboriosam cumque est dolor doloribus? Nulla expedita numquam alias quo perferendis hic veniam 
            optio, sint modi est laborum nemo saepe dignissimos fugit ea? Rem doloribus omnis similique id commodi nostrum veritatis labore excepturi quis 
            perspiciatis, modi nesciunt porro harum obcaecati ut saepe itaque provident sequi. Aut alias nostrum, enim velit odit ducimus, culpa assumenda 
            consequatur, dolores dignissimos illum soluta ducimus voluptatum culpa non quia ipsam similique maiores? Veniam iusto rem et recusandae cum 
            molestiae assumenda, amet at placeat laboriosam vero incidunt doloribus, dolor perspiciatis ducimus possimus enim molestiae neque fuga. 
            Rem ratione odit maxime sit mollitia. Saepe hic quisquam enim ea animi magni provident fuga sint, dicta maxime tempore hic beatae molestias 
            deleniti. Praesentium magnam dignissimos quae, expedita magnam repellendus itaque totam similique optio.

            Voluptates magnam magni quos nam minima mollitia, beatae dolor reiciendis quo explicabo a animi soluta ipsam architecto illo rem, 
            cumque delectus voluptatem est ducimus corrupti minus iste quos beatae voluptate, sit maxime eos explicabo porro fugit officia hic, 
            quas officia consequuntur eaque aut fuga animi architecto tempora. Officia voluptatum voluptatibus nemo ipsam qui nostrum dignissimos 
            libero perspiciatis? Natus harum repudiandae veniam doloremque eveniet, nemo quibusdam ipsam, inventore delectus commodi odio ipsa, 
            eligendi possimus earum officiis amet? Omnis voluptatibus harum quae ullam consequatur veniam rerum, debitis aut maxime cupiditate? 
            Unde aperiam incidunt quia, dolorum et earum ea culpa ut, nostrum minima saepe quasi nulla veritatis deserunt nemo, labore unde in 
            possimus numquam sapiente. Expedita recusandae repudiandae quos voluptatum mollitia consequatur doloribus fugit dolorem quisquam laboriosam, 
            laboriosam quisquam sunt nulla quibusdam in, suscipit dicta iusto aspernatur expedita eveniet accusantium illum quam corporis natus facilis, 
            reiciendis quo ab unde optio consequuntur quis fugit fugiat. Temporibus voluptatum dicta impedit adipisci officia aperiam deleniti nostrum quibusdam? 
            Adipisci ut veniam necessitatibus optio unde officia quia expedita, consequatur aliquam doloremque corrupti?
        """
    },
]
def get_date(post):
    return post['date']

def index(request):
    sorted_posts = sorted(posts,key=get_date)
    latest_posts = sorted_posts[-2:]
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })

def posts_page(request):
    return render(request,"blog/posts.html",{
        "posts":posts
    })

def post_detail(request,slug):
    post = next(post for post in posts if post['slug'] == slug)
    return render(request,"blog/post-detail.html",{
        "post":post
    })