@namespace
class SpriteKind:
    block = SpriteKind.create()
    落ちぷよ = SpriteKind.create()
def 浮遊してないか():
    global 地面ぷよcheck, 落ちぷよ一覧
    地面ぷよcheck = 29
    落ちぷよ一覧 = []
    for index in range(23):
        if 配列[地面ぷよcheck] == 0 and 配列[地面ぷよcheck - 6] > 0:
            配列[地面ぷよcheck] = 配列[地面ぷよcheck - 6]
            落ちぷよ一覧.append(地面ぷよcheck)
            配列[地面ぷよcheck - 6] = 0
        地面ぷよcheck += -1

def on_right_pressed():
    global 落ちぷよ場所
    if 配列[落ちぷよ場所 + 1] == 0:
        配列[落ちぷよ場所] = 0
        落ちぷよ場所 += 1
        配列[落ちぷよ場所] = 落下ぷよ種類
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def ぷよ消し判定():
    global 消すリスト, 消す場所, 消したかどうか, コンボ数
    消すリスト = []
    ぷよ消しリスト作成()
    消す場所 = 0
    if len(消すリスト) > 1:
        info.change_score_by(1)
        消したかどうか = 1
        コンボ数 += 1
        for index2 in range(len(消すリスト)):
            配列[消すリスト[消す場所]] = 0
            消す場所 += 1
    else:
        消したかどうか = -1
def ぷよ消しリスト作成():
    global x
    if 配列[落ちぷよ場所] > 0:
        消すリスト.unshift(落ちぷよ場所)
        x = 0
        while len(消すリスト) > x:
            if 消すリスト.index(消すリスト[x] + 1) == -1 and 配列[消すリスト[x] + 1] == 配列[消すリスト[x]]:
                消すリスト.append(消すリスト[x] + 1)
            if 消すリスト.index(消すリスト[x] + 6) == -1 and 配列[消すリスト[x] + 6] == 配列[消すリスト[x]]:
                消すリスト.append(消すリスト[x] + 6)
            if 消すリスト.index(消すリスト[x] - 1) == -1 and 配列[消すリスト[x] - 1] == 配列[消すリスト[x]]:
                消すリスト.append(消すリスト[x] - 1)
            if 消すリスト.index(消すリスト[x] - 6) == -1 and 配列[消すリスト[x] - 6] == 配列[消すリスト[x]]:
                消すリスト.append(消すリスト[x] - 6)
            x += 1

def on_left_pressed():
    global 落ちぷよ場所
    if 配列[落ちぷよ場所 - 1] == 0:
        配列[落ちぷよ場所] = 0
        落ちぷよ場所 += -1
        配列[落ちぷよ場所] = 落下ぷよ種類
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def ぷよ表示():
    global mySprite
    if 配列[checkぷよ] == -1:
        mySprite = sprites.create(img("""
                ........................
                            ..........bbbb..........
                            ........bbddddbb........
                            .......bddbbbbddb.......
                            ......bdbbddddbbdb......
                            .....bdbbdbbbbdbbdb.....
                            .....bdbdbddddbdbdb.....
                            .....cdbbdbbbbdbbdc.....
                            .....cbdbbddddbbdbc.....
                            .....efbddbbbbddbce.....
                            .....eeffbddddbccee.....
                            .....eeeeffcccceee......
                            .....ceeeeeeeeeeee......
                            .....ceeeeeeeeeeee......
                            .....feeeeeeeeeeee......
                            .....cceeeeeeeeeee......
                            ......feeeeeeeeeee......
                            .....6fceeeeeeeeee6.....
                            ....6776eeeeeeeee676....
                            ...6777666eeee6666776...
                            ..67768e67766777667776..
                            ...668ee7768867788666...
                            ......ee77eeee77ecee....
                            ......ee6eeeeee6eef.....
            """),
            SpriteKind.block)
        if checkぷよ < 6:
            mySprite.y = 10
            mySprite.destroy()
        if checkぷよ < 12 and checkぷよ >= 6:
            mySprite.y = 30
        if checkぷよ < 18 and checkぷよ >= 12:
            mySprite.y = 50
        if checkぷよ < 24 and checkぷよ >= 18:
            mySprite.y = 70
        if checkぷよ < 30 and checkぷよ >= 24:
            mySprite.y = 90
        if checkぷよ < 36 and checkぷよ >= 30:
            mySprite.y = 110
        if checkぷよ % 6 == 0:
            mySprite.x = 10
        if checkぷよ % 6 == 1:
            mySprite.x = 25
        if checkぷよ % 6 == 2:
            mySprite.x = 40
        if checkぷよ % 6 == 3:
            mySprite.x = 55
        if checkぷよ % 6 == 4:
            mySprite.x = 70
        if checkぷよ % 6 == 5:
            mySprite.x = 85
    if 配列[checkぷよ] == 1:
        mySprite = sprites.create(img("""
                . . . . . . . e c 7 . . . . . . 
                            . . . . e e e c 7 7 e e . . . . 
                            . . c e e e e c 7 e 2 2 e e . . 
                            . c e e e e e c 6 e e 2 2 2 e . 
                            . c e e e 2 e c c 2 4 5 4 2 e . 
                            c e e e 2 2 2 2 2 2 4 5 5 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 4 4 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                            c e e 2 2 2 2 2 2 2 2 2 2 4 2 e 
                            . e e e 2 2 2 2 2 2 2 2 2 4 e . 
                            . 2 e e 2 2 2 2 2 2 2 2 4 2 e . 
                            . . 2 e e 2 2 2 2 2 4 4 2 e . . 
                            . . . 2 2 e e 4 4 4 2 e e . . . 
                            . . . . . 2 2 e e e e . . . . .
            """),
            SpriteKind.落ちぷよ)
        if checkぷよ < 6:
            mySprite.y = 10
        if checkぷよ < 12 and checkぷよ >= 6:
            mySprite.y = 30
        if checkぷよ < 18 and checkぷよ >= 12:
            mySprite.y = 50
        if checkぷよ < 24 and checkぷよ >= 18:
            mySprite.y = 70
        if checkぷよ < 30 and checkぷよ >= 24:
            mySprite.y = 90
        if checkぷよ < 36 and checkぷよ >= 30:
            mySprite.y = 110
        if checkぷよ % 6 == 0:
            mySprite.x = 10
        if checkぷよ % 6 == 1:
            mySprite.x = 25
        if checkぷよ % 6 == 2:
            mySprite.x = 40
        if checkぷよ % 6 == 3:
            mySprite.x = 55
        if checkぷよ % 6 == 4:
            mySprite.x = 70
        if checkぷよ % 6 == 5:
            mySprite.x = 85
    if 配列[checkぷよ] == 2:
        mySprite = sprites.create(img("""
                4 4 4 . . 4 4 4 4 4 . . . . . . 
                            4 5 5 4 4 5 5 5 5 5 4 4 . . . . 
                            b 4 5 5 1 5 1 1 1 5 5 5 4 . . . 
                            . b 5 5 5 5 1 1 5 5 1 1 5 4 . . 
                            . b d 5 5 5 5 5 5 5 5 1 1 5 4 . 
                            b 4 5 5 5 5 5 5 5 5 5 5 1 5 4 . 
                            c d 5 5 5 5 5 5 5 5 5 5 5 5 5 4 
                            c d 4 5 5 5 5 5 5 5 5 5 5 1 5 4 
                            c 4 5 5 5 d 5 5 5 5 5 5 5 5 5 4 
                            c 4 d 5 4 5 d 5 5 5 5 5 5 5 5 4 
                            . c 4 5 5 5 5 d d d 5 5 5 5 5 b 
                            . c 4 d 5 4 5 d 4 4 d 5 5 5 4 c 
                            . . c 4 4 d 4 4 4 4 4 d d 5 d c 
                            . . . c 4 4 4 4 4 4 4 4 5 5 5 4 
                            . . . . c c b 4 4 4 b b 4 5 4 4 
                            . . . . . . c c c c c c b b 4 .
            """),
            SpriteKind.落ちぷよ)
        if checkぷよ < 6:
            mySprite.y = 10
        if checkぷよ < 12 and checkぷよ >= 6:
            mySprite.y = 30
        if checkぷよ < 18 and checkぷよ >= 12:
            mySprite.y = 50
        if checkぷよ < 24 and checkぷよ >= 18:
            mySprite.y = 70
        if checkぷよ < 30 and checkぷよ >= 24:
            mySprite.y = 90
        if checkぷよ < 36 and checkぷよ >= 30:
            mySprite.y = 110
        if checkぷよ % 6 == 0:
            mySprite.x = 10
        if checkぷよ % 6 == 1:
            mySprite.x = 25
        if checkぷよ % 6 == 2:
            mySprite.x = 40
        if checkぷよ % 6 == 3:
            mySprite.x = 55
        if checkぷよ % 6 == 4:
            mySprite.x = 70
        if checkぷよ % 6 == 5:
            mySprite.x = 85
def ぷよ表示全体():
    global checkぷよ
    checkぷよ = 0
    for index3 in range(36):
        ぷよ表示()
        checkぷよ += 1
mySprite: Sprite = None
checkぷよ = 0
x = 0
消したかどうか = 0
消す場所 = 0
消すリスト: List[number] = []
地面ぷよcheck = 0
y = 0
落ちぷよ一覧: List[number] = []
落下中判定 = 0
落下ぷよ種類 = 0
落ちぷよ場所 = 0
コンボ数 = 0
配列: List[number] = []
info.set_score(0)
puyonumber = 20
落ちぷよ処理中 = 0
scene.set_background_color(1)
配列 = [-1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    0,
    0,
    0,
    0,
    -1,
    -1,
    0,
    0,
    0,
    0,
    -1,
    -1,
    0,
    0,
    0,
    0,
    -1,
    -1,
    0,
    0,
    0,
    0,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1]
while True:
    コンボ数 = 0
    落ちぷよ場所 = 3
    落下ぷよ種類 = randint(1, 2)
    配列[落ちぷよ場所] = 落下ぷよ種類
    落下中判定 = 1
    while 落下中判定:
        ぷよ表示全体()
        pause(1000)
        sprites.destroy_all_sprites_of_kind(SpriteKind.落ちぷよ)
        if 配列[落ちぷよ場所 + 6] == 0:
            配列[落ちぷよ場所] = 0
            落ちぷよ場所 += 6
            配列[落ちぷよ場所] = 落下ぷよ種類
        else:
            if 落ちぷよ場所 < 7:
                game.over(False)
            else:
                配列[落ちぷよ場所] = 落下ぷよ種類
                落下中判定 = 0
    ぷよ消し判定()
    浮遊してないか()
    ぷよ表示全体()
    pause(1000)
    if len(落ちぷよ一覧) > 0:
        落ちぷよ処理中 = 1
        y = 0
        for index4 in range(len(落ちぷよ一覧)):
            落ちぷよ場所 = 落ちぷよ一覧[y]
            ぷよ消し判定()
            y += 1
        if len(落ちぷよ一覧) < y:
            浮遊してないか()
            ぷよ表示全体()
            落ちぷよ処理中 = 0

def on_forever():
    game.show_long_text(info.score(), DialogLayout.TOP)
forever(on_forever)
