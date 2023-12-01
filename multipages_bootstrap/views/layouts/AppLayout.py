import dash
from views.partials.Sidebar import Sidebar
from views.partials.Footer import Footer
from dash import html, dcc, callback, Input, Output, State

class AppLayout:
    @staticmethod
    def define_layout():
        return html.Div(
            children=[
                Sidebar.define_layout(),
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                dash.page_container
                            ],
                            id = 'content',
                        ),
                        Footer.define_layout()
                    ],
                    id = 'content-wrapper',
                    className='d-flex flex-column'
                )
            ],
            id='wrapper',
        )