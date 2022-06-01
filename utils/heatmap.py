try:
    from utils.vanilla_dataloader import load_data, percent_change_df
except:
    from vanilla_dataloader import load_data, percent_change_df
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox

metric = 'percent_change'


def get_color(x, df):
    global metric
    return 'g' if df.loc[x][metric]>=0 else 'r'

def get_heatmap(df):
    global metric
    plt.ioff()
    plt.style.use('dark_background')
    r1 = patches.Rectangle((12, 24),width=32,height=12,fill=True,facecolor='black',linewidth=2,edgecolor='white')
    r2 = patches.Rectangle((12, 4),width=20,height=20,fill=True,facecolor='black',linewidth=2,edgecolor='white')
    r3 = patches.Rectangle((32, 12),width=12,height=12,fill=True,facecolor='black',linewidth=2,edgecolor='white')
    r4 = patches.Rectangle((32, 4),width=12,height=8,fill=True,facecolor='black',linewidth=2,edgecolor='white')

    r5 = patches.Rectangle((52, 16),width=20,height=20,fill=True,facecolor='black',linewidth=2,edgecolor='white')
    r6 = patches.Rectangle((52, 4),width=12,height=12,fill=True,facecolor='black',linewidth=2,edgecolor='white')
    r7 = patches.Rectangle((64, 4),width=8,height=12,fill=True,facecolor='black',linewidth=2,edgecolor='white')

    r8 = patches.Rectangle((80, 24),width=12,height=12,fill=True,facecolor='black',linewidth=2,edgecolor='white')
    r9 = patches.Rectangle((92, 24),width=8,height=12,fill=True,facecolor='black',linewidth=2,edgecolor='white')

    r10 = patches.Rectangle((80, 4),width=12,height=12,fill=True,facecolor='black',linewidth=2,edgecolor='white')
    r11 = patches.Rectangle((92, 4),width=8,height=12,fill=True,facecolor='black',linewidth=2,edgecolor='white')

    r12 = patches.Rectangle((108, 16),width=20,height=20,fill=True,facecolor='black',linewidth=2,edgecolor='white')
    r13 = patches.Rectangle((108, 4),width=12,height=12,fill=True,facecolor='black',linewidth=2,edgecolor='white')
    r14 = patches.Rectangle((120, 4),width=8,height=12,fill=True,facecolor='black',linewidth=2,edgecolor='white')

    try:
        i1 = AnnotationBbox(OffsetImage(mpimg.imread('./images/apple.png'), zoom=0.7), (22, 18))
        i2 = AnnotationBbox(OffsetImage(mpimg.imread('./images/nvidia.png'), zoom=0.8), (24, 30))
        i3 = AnnotationBbox(OffsetImage(mpimg.imread('./images/intel.png'), zoom=1), (38, 21))
        i4 = AnnotationBbox(OffsetImage(mpimg.imread('./images/qualcomm.png'), zoom=1), (38, 10.5))

        i5 = AnnotationBbox(OffsetImage(mpimg.imread('./images/microsoft.png'), zoom=0.6), (62, 30))
        i6 = AnnotationBbox(OffsetImage(mpimg.imread('./images/google.png'), zoom=0.6), (58, 13))
        i7 = AnnotationBbox(OffsetImage(mpimg.imread('./images/meta2.png'), zoom=1.25), (68, 13))

        i8 = AnnotationBbox(OffsetImage(mpimg.imread('./images/amazon.png'), zoom=0.7), (86, 13))
        i9 = AnnotationBbox(OffsetImage(mpimg.imread('./images/walmart.jpeg'), zoom=0.6), (96, 13))

        i10 = AnnotationBbox(OffsetImage(mpimg.imread('./images/tesla.png'), zoom=0.5), (86, 32.5))
        i11 = AnnotationBbox(OffsetImage(mpimg.imread('./images/ea.png'), zoom=0.4), (96, 33))

        i12 = AnnotationBbox(OffsetImage(mpimg.imread('./images/uhg.png'), zoom=0.9), (118, 30.5))
        i13 = AnnotationBbox(OffsetImage(mpimg.imread('./images/azn.png'), zoom=0.6), (114, 13))
        i14 = AnnotationBbox(OffsetImage(mpimg.imread('./images/cvs.png'), zoom=0.8), (124, 13))
    except:
        i1 = AnnotationBbox(OffsetImage(mpimg.imread('../images/apple.png'), zoom=0.7), (22, 18))
        i2 = AnnotationBbox(OffsetImage(mpimg.imread('../images/nvidia.png'), zoom=0.8), (24, 30))
        i3 = AnnotationBbox(OffsetImage(mpimg.imread('../images/intel.png'), zoom=1), (38, 21))
        i4 = AnnotationBbox(OffsetImage(mpimg.imread('../images/qualcomm.png'), zoom=1), (38, 10.5))

        i5 = AnnotationBbox(OffsetImage(mpimg.imread('../images/microsoft.png'), zoom=0.6), (62, 30))
        i6 = AnnotationBbox(OffsetImage(mpimg.imread('../images/google.png'), zoom=0.6), (58, 13))
        i7 = AnnotationBbox(OffsetImage(mpimg.imread('../images/meta2.png'), zoom=1.25), (68, 13))

        i8 = AnnotationBbox(OffsetImage(mpimg.imread('../images/amazon.png'), zoom=0.7), (86, 13))
        i9 = AnnotationBbox(OffsetImage(mpimg.imread('../images/walmart.jpeg'), zoom=0.6), (96, 13))

        i10 = AnnotationBbox(OffsetImage(mpimg.imread('../images/tesla.png'), zoom=0.5), (86, 32.5))
        i11 = AnnotationBbox(OffsetImage(mpimg.imread('../images/ea.png'), zoom=0.4), (96, 33))

        i12 = AnnotationBbox(OffsetImage(mpimg.imread('../images/uhg.png'), zoom=0.9), (118, 30.5))
        i13 = AnnotationBbox(OffsetImage(mpimg.imread('../images/azn.png'), zoom=0.6), (114, 13))
        i14 = AnnotationBbox(OffsetImage(mpimg.imread('../images/cvs.png'), zoom=0.8), (124, 13))




    r = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14]
    i = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14]
    fig, ax = plt.subplots(1, figsize=(140,40), facecolor="black", edgecolor="black")
    for rx in r:
        ax.add_patch(rx)
    for ix in i:
        ax.add_artist(ix)
  
    ax.annotate(text='AAPL', xy=(22, 9), color='w', weight='semibold', fontsize=100, ha='center', va='center')
    ax.annotate(text='NVDA', xy=(34, 31.5), color='w', weight='semibold', fontsize=100, ha='center', va='center')
    ax.annotate(text='INTC', xy=(38, 17), color='w', weight='semibold', fontsize=100, ha='center', va='center')
    ax.annotate(text='QCOM', xy=(38, 8), color='w', weight='semibold', fontsize=90, ha='center', va='center')

    ax.annotate(text='MSFT', xy=(62, 22), color='w', weight='semibold', fontsize=100, ha='center', va='center')
    ax.annotate(text='GOOGL', xy=(58, 9), color='w', weight='semibold', fontsize=90, ha='center', va='center')
    ax.annotate(text='FB', xy=(68, 9), color='w', weight='semibold', fontsize=80, ha='center', va='center')

    ax.annotate(text='AMZN', xy=(86, 9), color='w', weight='semibold', fontsize=80, ha='center', va='center')
    ax.annotate(text='WMT', xy=(96, 9), color='w', weight='semibold', fontsize=80, ha='center', va='center')

    ax.annotate(text='TSLA', xy=(86, 28), color='w', weight='semibold', fontsize=80, ha='center', va='center')
    ax.annotate(text='EA', xy=(96, 28), color='w', weight='semibold', fontsize=80, ha='center', va='center')

    ax.annotate(text='UNH', xy=(118, 25), color='w', weight='semibold', fontsize=100, ha='center', va='center')
    ax.annotate(text='AZN', xy=(114, 9), color='w', weight='semibold', fontsize=90, ha='center', va='center')
    ax.annotate(text='CVS', xy=(124, 9), color='w', weight='semibold', fontsize=80, ha='center', va='center')

    #===============================================================================================================
    c = -3
    ax.annotate(text=str(df.loc['AAPL'][metric])+'%', xy=(22, 7), color=get_color('AAPL', df), weight='semibold', fontsize=100, ha='center', va='center')
    ax.annotate(text=str(df.loc['NVDA'][metric])+'%', xy=(34, 28.5), color=get_color('NVDA', df), weight='semibold', fontsize=100, ha='center', va='center')
    ax.annotate(text=str(df.loc['INTC'][metric])+'%', xy=(38, 14.3), color=get_color('INTC', df), weight='semibold', fontsize=100, ha='center', va='center')
    ax.annotate(text=str(df.loc['QCOM'][metric])+'%', xy=(38, 5.3), color=get_color('QCOM', df), weight='semibold', fontsize=90, ha='center', va='center')

    ax.annotate(text=str(df.loc['MSFT'][metric])+'%', xy=(62, 20), color=get_color('MSFT', df), weight='semibold', fontsize=100, ha='center', va='center')
    ax.annotate(text=str(df.loc['GOOGL'][metric])+'%', xy=(58, 7), color=get_color('GOOGL', df), weight='semibold', fontsize=90, ha='center', va='center')
    ax.annotate(text=str(df.loc['FB'][metric])+'%', xy=(68, 7), color=get_color('FB', df), weight='semibold', fontsize=80, ha='center', va='center')

    ax.annotate(text=str(df.loc['AMZN'][metric])+'%', xy=(86, 7), color=get_color('AMZN', df), weight='semibold', fontsize=80, ha='center', va='center')
    ax.annotate(text=str(df.loc['WMT'][metric])+'%', xy=(96, 7), color=get_color('WMT', df), weight='semibold', fontsize=80, ha='center', va='center')

    ax.annotate(text=str(df.loc['TSLA'][metric])+'%', xy=(86, 25), color=get_color('TSLA',df), weight='semibold', fontsize=80, ha='center', va='center')
    ax.annotate(text=str(df.loc['EA'][metric])+'%', xy=(96, 25), color=get_color('EA', df), weight='semibold', fontsize=80, ha='center', va='center')

    ax.annotate(text=str(df.loc['UNH'][metric])+'%', xy=(118, 22), color=get_color('UNH', df), weight='semibold', fontsize=100, ha='center', va='center')
    ax.annotate(text=str(df.loc['AZN'][metric])+'%', xy=(114, 7), color=get_color('AZN', df), weight='semibold', fontsize=90, ha='center', va='center')
    ax.annotate(text=str(df.loc['CVS'][metric])+'%', xy=(124, 7), color=get_color('CVS', df), weight='semibold', fontsize=80, ha='center', va='center')

    ax.set_xlim(0,140)
    ax.set_ylim(0,40)
    
    try:
        output_path = './output/overview.png'
        plt.savefig(output_path, bbox_inches='tight')
    except:
        output_path = '../output/overview.png'
        plt.savefig(output_path, bbox_inches='tight')
    plt.close('all')
    return output_path


if __name__=="__main__":
    sector_market_share = {'AAPL': ['Electronics Technology', 2455053795328],
     'AMZN': ['Retail Trade', 1167926362112],
     'AZN': ['Healthcare', 208860000000],
     'CVS': ['Healthcare', 129431887872],
     'EA': ['Consumer Durables', 39177392128],
     'FB': ['Technology Servies', 542804836352],
     'GOOGL': ['Technology Servies', 1482231906304 ],
     'INTC': ['Electronics Technology', 181184856064],
     'MSFT': ['Technology Servies', 2051480354816],
     'NVDA': ['Electronics Technology', 468770127872],
     'QCOM': ['Electronics Technology', 156531195904],
     'TSLA': ['Consumer Durables', 762865975296],
     'UNH': ['Healthcare', 475756396544],
     'WMT': ['Retail Trade', 356388110336]}
    
    stock_list = list(sector_market_share.keys())
    data_list, ti_list = load_data(stock_list)
    stock_df = percent_change_df(data_list, sector_market_share)

    print(get_heatmap(stock_df))
