from flet import *
from custom_checkbox import CustomCheckBox



def main(page: Page):
    page.title = "ToDo List"
    BG = '#57233A' #wine berry
    FWG = '#A67F78' #elephant
    FG = '#AE4951' #HIPPIE PINK
    NEW = '#B98D72'
    SMOKYBLACK = '#161B1F' #gun metal

    circle = Stack(
    controls=[
      Container(
        width=100,
        height=100,
        border_radius=50,
        bgcolor='white12'
        ),
      Container(
                  gradient=SweepGradient(
                      center=alignment.center,
                      start_angle=0.0,
                      end_angle=3,
                      stops=[0.5,0.5],
                  colors=['#00000000', SMOKYBLACK],
                  ),
                  width=100,
                  height=100,
                  border_radius=50,
                  content=Row(alignment='center',
                      controls=[
                        Container(padding=padding.all(5),
                          bgcolor=BG,
                          width=90,height=90,
                          border_radius=50,
                          content=Container(bgcolor=FG,
                            height=80,width=80,
                            border_radius=40,
                          content=CircleAvatar(opacity=0.8,
                foreground_image_url="https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
            )
                          )
                          )
                      ],
                  ),
              ),
      
    ]
  )


    def restore(e):
        page_2.controls[0].width = 350
        page_2.controls[0].scale = transform.Scale(1, alignment=alignment.center_right)
        page_2.controls[0].border_radius = 25
        page_2.update()

    
    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(0.8, alignment=alignment.center_right)
        page_2.controls[0].border_radius = border_radius.only(
            top_left=35, 
            top_right=0,
            bottom_left=35,
            bottom_right=0
        )
        page_2.update()

    



    create_task_view = Container(
        content=Container(
            padding = padding.only(top=20, left=10),
            content= Icon(icons.ARROW_BACK_SHARP),
                on_click= lambda _: page.go('/')
        )
    )

    tasks = Column(
        height=300,
        scroll='auto',
        # controls= Row(
        #     controls=Text()
        # )
    )

    for i in range(10):
        tasks.controls.append(
            Container(
                height=70,
                width=400,
                bgcolor= SMOKYBLACK,
                border_radius=25,
                padding=padding.only(left=20, top=25),
                content= CustomCheckBox(
                    color=FWG,
                    size=20,
                    font_size=15,
                    label='Create Task'
                )
            ),
        )

    categories_card = Row(
        scroll='auto'
    )
    categories = ['Miscelaneous',  'School', 'Work']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                bgcolor=SMOKYBLACK,
                height = 110, 
                width = 170,
                padding=15,
                border_radius=20,
                content=Column(
                    controls=[   
                    Text('20 Tasks'),
                    Text(category),
                    Container(
                        width=160,
                        height=5,
                        border_radius=20,
                        bgcolor='white12',
                        padding=padding.only(right=i*40),
                        content= Container(
                            bgcolor=FWG
                        )
                    ),
                    ]
                )
            )
        )


    first_page_content = Container(
        content=Column(
            controls=[
                Row( 
                    alignment = 'spaceBetween',
                    controls=[
                        Container(
                            content=
                            Icon(icons.MENU),
                            on_click= lambda e: shrink(e)
                        ), 
                        Row(
                            controls=[
                                Icon(icons.SEARCH),
                                Icon(icons.NOTIFICATIONS_OUTLINED)
                            ]
                        )
                    ]
                ),
                Container(height = 20),
                Text('What\'s up, \n Michael', 
                     size=25,
                     weight='bold',
                     ),
                Text('CATEGORIES', weight=FontWeight.W_400),
                Container(
                    padding=padding.only(top=10, bottom=20),
                    content= categories_card
                ),
                Container(height = 10),
                Text("TODAY'S TASKS", weight=FontWeight.W_400),
                Stack(
                    controls=[
                       tasks,
                       FloatingActionButton(
                           right = 10,
                           bottom = 3,
                           icon=icons.ADD,
                           on_click=lambda _:page.go('/create_task'),
                           bgcolor=NEW
                       )
                    ]
                )
            ]
        )
    )

    page_1 = Container(
        width=350,
        height=850,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50, top=60, right=200),
        content=Column(
            controls=[
                Row( 
                    alignment='end',
                controls=[
                    Container(
                    content= Icon(icons.ARROW_BACK_SHARP),
                    on_click= lambda e:restore(e)
                ),
                ]
                ),
                Container(height=20),
                circle,
                Text('Michael \n Uche ', 
                     size=25,
                     weight='bold',
                     text_align= 'left',
                    ),
                Container(height=20),
                Row(
                    controls=[
                        Icon(icons.FAVORITE_BORDER_SHARP, color='white40'),
                        Text('Templates', size=14, weight=FontWeight.W_300, color='white')
                    ]
                ),
                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.CARD_TRAVEL_OUTLINED, color='white40'),
                        Text('Templates', size=14, weight=FontWeight.W_300, color='white')
                    ]
                ),
                Container(height=5),
                Row(
                    controls=[
                        Icon(icons.SETTINGS_OUTLINED, color='white40'),
                        Text('Settings', size=14, weight=FontWeight.W_300, color='white')
                    ]
                )    
            ]
        )
    )
    page_2 = Row(
        alignment='end',
        controls=[
            Container(
                width = 350,
                height = 750,
                bgcolor = FG,
                border_radius=35,
                animate = animation.Animation(600, AnimationCurve.EASE_IN_CIRC),
                animate_scale=animation.Animation(400, AnimationCurve.DECELERATE),
                padding = padding.only(
                    top=50,
                    left=20,
                    right=20,
                    bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_content
                    ]
                )
            )
        ]
    )

    Page_container = Container(
        width = 350,
        height = 750,
        bgcolor = BG,
        border_radius=35,
        content= Stack(
            controls=[
                page_1,
                page_2
            ]
        )
    )

    pages = {
        '/': View(
                "/",
                [
                    Page_container
                ],
            ),
        '/create_task': View(
                "/create_task",
                [
                    create_task_view
                ],
            ) 
    }
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            pages[page.route]
        )


    page.on_route_change = route_change
    page.go(page.route)


app(target=main)
