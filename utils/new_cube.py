import ipywidgets as ipw

def cube_factory(sector):
    key_list = ['Electronics Technology', 'Technology Servies', 'Consumer Durables', 'Retail Trade', 'Healthcare']
    values = [round(sector[key],2) for key in key_list]
    
    css_code = '<style>\
    .spinner div {\
        position: absolute;\
        width: 200px;\
        height: 200px;\
        border: 1px solid #ccc;\
        background: rgba(37,37,37,0.8);\
        box-shadow: inset 0 0 20px rgba(0,0,0,0.2);\
        text-align: center;\
        line-height: 50px;\
        font-size: 100px;\
    }\
    .spinner .face1 { \
        -webkit-transform: translateZ(100px);\
        -ms-transform: translateZ(100px);\
        transform: translateZ(100px);\
    }\
    .spinner .face2 { \
        -webkit-transform: rotateY(90deg) translateZ(100px); \
        -ms-transform: rotateY(90deg) translateZ(100px); \
        transform: rotateY(90deg) translateZ(100px); \
    }\
    .spinner .face3 { \
        -webkit-transform: rotateY(90deg) rotateX(90deg) translateZ(100px); \
        -ms-transform: rotateY(90deg) rotateX(90deg) translateZ(100px); \
        transform: rotateY(90deg) rotateX(90deg) translateZ(100px); \
    }\
    .spinner .face4 { \
        -webkit-transform: rotateY(180deg) rotateZ(90deg) translateZ(100px); \
        -ms-transform: rotateY(180deg) rotateZ(90deg) translateZ(100px); \
        transform: rotateY(180deg) rotateZ(90deg) translateZ(100px); \
    }\
    .spinner .face5 { \
        -webkit-transform: rotateY(-90deg) rotateZ(90deg) translateZ(100px); \
        -ms-transform: rotateY(-90deg) rotateZ(90deg) translateZ(100px); \
        transform: rotateY(-90deg) rotateZ(90deg) translateZ(100px); \
    }\
    .spinner .face6 { \
        -webkit-transform: rotateX(-90deg) translateZ(100px); \
        -ms-transform: rotateX(-90deg) translateZ(100px); \
        transform: rotateX(-90deg) translateZ(100px); \
    }\
    .spinner {\
        -webkit-animation: spincube 12s ease-in-out infinite;\
        animation: spincube 12s ease-in-out infinite;\
        -webkit-transform-style: preserve-3d;\
        -ms-transform-style: preserve-3d;\
        transform-style: preserve-3d;\
        -webkit-transform-origin: 150px 150px 0;\
        -ms-transform-origin: 150px 150px 0;\
        transform-origin: 150px 150px 0;\
    }\
    @-webkit-keyframes spincube {\
        16%      { -webkit-transform: rotateY(-90deg);                }\
        33%      { -webkit-transform: rotateY(-90deg) rotateZ(90deg); }\
        50%      { -webkit-transform: rotateY(180deg) rotateZ(90deg); }\
        66%      { -webkit-transform: rotateY(90deg) rotateX(90deg);  }\
        83%      { -webkit-transform: rotateX(90deg);                 }\
    }\
    @keyframes spincube {\
        16%      { -ms-transform: rotateY(-90deg); transform: rotateY(-90deg); }\
        33%      { -ms-transform: rotateY(-90deg) rotateZ(90deg); transform: rotateY(-90deg) rotateZ(90deg); }\
        50%      { -ms-transform: rotateY(180deg) rotateZ(90deg); transform: rotateY(180deg) rotateZ(90deg); }\
        66%      { -ms-transform: rotateY(90deg) rotateX(90deg); transform: rotateY(90deg) rotateX(90deg); }\
        83%      { -ms-transform: rotateX(90deg); transform: rotateX(90deg); }\
    }\
    </style>'
    
    html_code='<body>\
            <div id="stage" style="width: 200px; height: 200px;">\
                <div class="spinner">\
                    <div class="face1" style="color:lightgreen;font-size:18px"> <br>Electronics Technology <br> {0}%</div>\
                    <div class="face2" style="color:Khaki;font-size:18px"> <br>Technology Servies <br> {1}%</div>\
                    <div class="face3" style="color:DodgerBlue;font-size:18px"> <br>Consumer Durables <br> {2}%</div>\
                    <div class="face4" style="color:white;font-size:18px"> <br>Retail Trade <br> {3}%</div>\
                    <div class="face5" style="color:LightCoral;font-size:18px"> <br>Healthcare <br> {4}%</div>\
                    <div class="face6" style="color:green;font-size:18px"></div>\
                </div>\
            </div>\
    </body>'.format(values[0], values[1], values[2], values[3], values[4])
    return ipw.HTML(css_code + html_code)