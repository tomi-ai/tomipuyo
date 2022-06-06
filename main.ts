namespace SpriteKind {
    export const block = SpriteKind.create()
    export const 落ちぷよ = SpriteKind.create()
}
function 浮遊してないか () {
    地面ぷよcheck = 29
    落ちぷよ一覧 = []
    for (let index = 0; index < 23; index++) {
        if (ぷよ盤面[地面ぷよcheck] == 0 && ぷよ盤面[地面ぷよcheck - 6] > 0) {
            ぷよ盤面[地面ぷよcheck] = ぷよ盤面[地面ぷよcheck - 6]
            落ちぷよ一覧.push(地面ぷよcheck)
            ぷよ盤面[地面ぷよcheck - 6] = 0
        }
        地面ぷよcheck += -1
    }
}
function ぷよ消し判定 () {
    消すリスト = []
    ぷよ消しリスト作成()
    消す場所 = 0
    if (消すリスト.length > 1) {
        info.changeScoreBy(1)
        消したかどうか += 1
        コンボ数 += 1
        for (let index = 0; index < 消すリスト.length; index++) {
            ぷよ盤面[消すリスト[消す場所]] = 0
            消す場所 += 1
        }
    } else {
    	
    }
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    if (操作可能 == 1 && ぷよ盤面[落ちぷよ場所 - 1] == 0) {
        ぷよ盤面[落ちぷよ場所] = 0
        落ちぷよ場所 += -1
        ぷよ盤面[落ちぷよ場所] = 落下ぷよ種類
    }
})
function ぷよ消しリスト作成 () {
    if (ぷよ盤面[落ちぷよ場所] > 0) {
        消すリスト.unshift(落ちぷよ場所)
        x = 0
        while (消すリスト.length > x) {
            if (消すリスト.indexOf(消すリスト[x] + 1) == -1 && ぷよ盤面[消すリスト[x] + 1] == ぷよ盤面[消すリスト[x]]) {
                消すリスト.push(消すリスト[x] + 1)
            }
            if (消すリスト.indexOf(消すリスト[x] + 6) == -1 && ぷよ盤面[消すリスト[x] + 6] == ぷよ盤面[消すリスト[x]]) {
                消すリスト.push(消すリスト[x] + 6)
            }
            if (消すリスト.indexOf(消すリスト[x] - 1) == -1 && ぷよ盤面[消すリスト[x] - 1] == ぷよ盤面[消すリスト[x]]) {
                消すリスト.push(消すリスト[x] - 1)
            }
            if (消すリスト.indexOf(消すリスト[x] - 6) == -1 && ぷよ盤面[消すリスト[x] - 6] == ぷよ盤面[消すリスト[x]]) {
                消すリスト.push(消すリスト[x] - 6)
            }
            x += 1
        }
    }
}
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    if (操作可能 == 1 && ぷよ盤面[落ちぷよ場所 + 1] == 0) {
        ぷよ盤面[落ちぷよ場所] = 0
        落ちぷよ場所 += 1
        ぷよ盤面[落ちぷよ場所] = 落下ぷよ種類
    }
})
function 落ちぷよ連鎖 () {
    消したかどうか = 0
    pause(1000)
    if (落ちぷよ一覧.length > 0) {
        落ちぷよ処理中 = 1
        y = 0
        while (落ちぷよ一覧.length > y) {
            落ちぷよ場所 = 落ちぷよ一覧[y]
            ぷよ消し判定()
            y += 1
        }
    }
    pause(1000)
    sprites.destroyAllSpritesOfKind(SpriteKind.落ちぷよ)
    浮遊してないか()
    ぷよ表示全体()
    落ちぷよ処理中 = 0
}
function ぷよ表示全体 () {
    checkぷよ = 0
    for (let index = 0; index < 36; index++) {
        ぷよを表示する()
        checkぷよ += 1
    }
}
function ぷよを表示する () {
    if (ぷよ盤面[checkぷよ] == 1) {
        mySprite = sprites.create(img`
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
            `, SpriteKind.落ちぷよ)
        if (checkぷよ < 6) {
            mySprite.y = 10
        }
        if (checkぷよ < 12 && checkぷよ >= 6) {
            mySprite.y = 30
        }
        if (checkぷよ < 18 && checkぷよ >= 12) {
            mySprite.y = 50
        }
        if (checkぷよ < 24 && checkぷよ >= 18) {
            mySprite.y = 70
        }
        if (checkぷよ < 30 && checkぷよ >= 24) {
            mySprite.y = 90
        }
        if (checkぷよ < 36 && checkぷよ >= 30) {
            mySprite.y = 110
        }
        if (checkぷよ % 6 == 0) {
            mySprite.x = 10
        }
        if (checkぷよ % 6 == 1) {
            mySprite.x = 25
        }
        if (checkぷよ % 6 == 2) {
            mySprite.x = 40
        }
        if (checkぷよ % 6 == 3) {
            mySprite.x = 55
        }
        if (checkぷよ % 6 == 4) {
            mySprite.x = 70
        }
        if (checkぷよ % 6 == 5) {
            mySprite.x = 85
        }
    }
    if (ぷよ盤面[checkぷよ] == 2) {
        mySprite = sprites.create(img`
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
            `, SpriteKind.落ちぷよ)
        if (checkぷよ < 6) {
            mySprite.y = 10
        }
        if (checkぷよ < 12 && checkぷよ >= 6) {
            mySprite.y = 30
        }
        if (checkぷよ < 18 && checkぷよ >= 12) {
            mySprite.y = 50
        }
        if (checkぷよ < 24 && checkぷよ >= 18) {
            mySprite.y = 70
        }
        if (checkぷよ < 30 && checkぷよ >= 24) {
            mySprite.y = 90
        }
        if (checkぷよ < 36 && checkぷよ >= 30) {
            mySprite.y = 110
        }
        if (checkぷよ % 6 == 0) {
            mySprite.x = 10
        }
        if (checkぷよ % 6 == 1) {
            mySprite.x = 25
        }
        if (checkぷよ % 6 == 2) {
            mySprite.x = 40
        }
        if (checkぷよ % 6 == 3) {
            mySprite.x = 55
        }
        if (checkぷよ % 6 == 4) {
            mySprite.x = 70
        }
        if (checkぷよ % 6 == 5) {
            mySprite.x = 85
        }
    }
}
let mySprite: Sprite = null
let checkぷよ = 0
let y = 0
let x = 0
let 消す場所 = 0
let 消すリスト: number[] = []
let 落ちぷよ一覧: number[] = []
let 地面ぷよcheck = 0
let 消したかどうか = 0
let 落下中判定 = 0
let 操作可能 = 0
let 落下ぷよ種類 = 0
let 落ちぷよ場所 = 0
let コンボ数 = 0
let 落ちぷよ処理中 = 0
let ぷよ盤面: number[] = []
info.setScore(0)
let puyonumber = 20
scene.setBackgroundColor(1)
scene.setBackgroundImage(assets.image`myImage2`)
ぷよ盤面 = [
-1,
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
-1
]
while (true) {
    while (落ちぷよ処理中 == 1) {
        pause(1000)
        if (落ちぷよ処理中 != 1) {
            break;
        }
    }
    コンボ数 = -1
    落ちぷよ場所 = 3
    落下ぷよ種類 = randint(1, 2)
    操作可能 = 1
    ぷよ盤面[落ちぷよ場所] = 落下ぷよ種類
    落下中判定 = 1
    while (落下中判定) {
        ぷよ表示全体()
        pause(1000)
        sprites.destroyAllSpritesOfKind(SpriteKind.落ちぷよ)
        if (ぷよ盤面[落ちぷよ場所 + 6] == 0) {
            ぷよ盤面[落ちぷよ場所] = 0
            落ちぷよ場所 += 6
            ぷよ盤面[落ちぷよ場所] = 落下ぷよ種類
        } else if (落ちぷよ場所 < 7) {
            game.over(false)
        } else {
            操作可能 = 0
            ぷよ盤面[落ちぷよ場所] = 落下ぷよ種類
            落下中判定 = 0
        }
    }
    消したかどうか = 0
    ぷよ消し判定()
    浮遊してないか()
    ぷよ表示全体()
    while (消したかどうか > 0) {
        落ちぷよ連鎖()
    }
    if (コンボ数 > 0) {
        story.printText("" + convertToText(コンボ数) + "コンボ", 10, 10, 15)
    }
}
forever(function () {
    game.showLongText(info.score(), DialogLayout.Top)
})
