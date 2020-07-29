from const import CATEGORIES_MAP, INVERT_CATEGORIES_MAP
import numpy as np

def _safe_get(idx):
    try:
        return INVERT_CATEGORIES_MAP[idx]
    except:
        return idx

def draw_md_table(scores):
    """
    sample input:
    {
        'VGG16': [0.739 ,0.786 ,0.721 ,0.755 ,0.776 ,0.774 ,0.683 ,0.884],
        'standard aug': [0.731 ,0.779 ,0.721 ,0.771 ,0.774 ,0.755 ,0.690 ,0.865],
        'GAN v1': [0.744 ,0.774 ,0.736 ,0.772 ,0.775 ,0.757 ,0.695 ,0.878],
    }
    """
    table = '|  |'
    for name in scores.keys():
        table += ' {} |'.format(name)

    table += '\n|'
    for i in range(len(scores) + 1):
        table += '--|'

    table += '\n'
    head = scores[list(scores.keys())[0]]
    len_head = len(head)
    avgs = [sum(v)/len_head for v in scores.values()]
    for i in range(len_head):
        # use i + 1 because we don't care No Finding case 
        table += '| ' + _safe_get(i) + ' |'
        # find the best score value
        best = 0
        row = ''
        for name in scores.keys():
            point = round(scores[name][i], 3)
            if point > best:
                best = point
            row += ' {} |'.format(point)
        row = row.replace(str(best), '**{}**'.format(best))
        table += row + '\n'
    row = '| **Average** |'
    best = 0
    for avg in avgs:
        avg = round(avg, 3)
        if avg > best:
            best = avg
        row += ' {} |'.format(avg)
    row = row.replace(str(best), '**{}**'.format(best))
    table += row + '\n'
    return table



t = draw_md_table(
    {
    'VGG16 + standard augment': [
        # 0.6786879452004883,
        # 0.6752725029828712,
        # 0.7354756531768718,
        # 0.7941096148413221,
        # 0.7013054341871434,
        # 0.753290263188177,
        # 0.7668212981593264,
        # 0.6395236344092106,
        # 0.6843162670123136,
        # 0.8765715667311411,
        # 0.7416795865633075,
        # 0.6375227444192962,
        0.48576365663322185,
        0.45813920655089646,
        0.6845064468399916
   ],
    'Ours': [
        # 0.6995164963290886,
        # 0.7197910978988453,
        # 0.765346772980292,
        # 0.8018193803559658,
        # 0.7259189481701206,
        # 0.7455557199454226,
        # 0.7619867352261718,
        # 0.6768295097734152,
        # 0.7019053791315619,
        # 0.8791908446163765,
        # 0.7356810631229236,
        # 0.6856077752629476,
        0.7350836120401338,
        0.45963574756459125,
        0.6983090255759883
    ],
    'BAGAN': [
        # 0.6947545134903719,
        # 0.7022861938562964,
        # 0.757531718569781,
        # 0.7859920896506263,
        # 0.7289734236581553,
        # 0.7296526442110107,
        # 0.7426447574334898,
        # 0.6480269299312609,
        # 0.6835093972780297,
        # 0.8937217923920052,
        # 0.6964562569213731,
        # 0.5811920294678916,
        0.55103121516165,
        0.477989552449527,
        0.5349397590361447
        ]
    }
)
print(t)
