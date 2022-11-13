import re
import json

cards_string = """
<!--
==000: Imperialdramon==
{{Card Infobox DDCB-DM
 |name=Imperialdramon
 |name_link=Imperialdramon Dragon Mode
 |name_jp=インペリアルドラモン
 |number=000
 |level=U
 |specialty=Fire
 |hp=1900
 |dp=60
 |pp=10
 |c_attack=Mega Fire
 |c_attack_jp=メガデス
 |c_attack_jp_roman=Mega Death
 |c_pow=980
 |t_attack=Eternal Zeal
 |t_attack_jp=エターナルジール
 |t_attack_jp_roman=
 |t_pow=670
 |x_attack=Shining Blade
 |x_attack_jp=スプレンダーブレード
 |x_attack_jp_roman=Splendor Blade
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=Add number of DP Cards in DP Slot x100 to own Attack Power.
}}
{{-}}

==001: Omnimon I==
{{Card Infobox DDCB-DM
 |name=Omnimon I
 |name_link=Omnimon
 |name_jp=オメガモンI
 |name_jp_roman=Omegamon I
 |number=001
 |level=U
 |specialty=Fire
 |hp=1800
 |dp=60
 |pp=20
 |c_attack=Transcendent Sword
 |c_attack_jp=グレイソード
 |c_attack_jp_roman=Grey Sword
 |c_pow=960
 |t_attack=Garuru Cannon
 |t_attack_jp=ガルルキャノン
 |t_attack_jp_roman=
 |t_pow=560
 |x_attack=Double Shot
 |x_attack_jp=ダブルトレント
 |x_attack_jp_roman=Double Torrent
 |x_pow=0
 |x_effect={{button|x}} Counter
 |support=Changes own Specialty to Fire. Boost own Attack Power +100.
}}
{{-}}

==002: WarGreymon==
{{Card Infobox DDCB-DM
 |name=WarGreymon
 |name_jp=ウォーグレイモン
 |number=002
 |level=U
 |specialty=Fire
 |hp=1650
 |dp=50
 |pp=20
 |c_attack=Terra Force
 |c_attack_jp=ガイアフォース
 |c_attack_jp_roman=Gaia Force
 |c_pow=900
 |t_attack=Great Tornado
 |t_attack_jp=グレートトルネード
 |t_attack_jp_roman=
 |t_pow=670
 |x_attack=Dramon Cutter
 |x_attack_jp=ドラモンキラー
 |x_attack_jp_roman=Dramon Killer
 |x_pow=380
 |x_effect=Ice Foe x3
 |support=Add number of Cards in Hand x100 to own Attack Power.
}}
{{-}}

==003: Phoenixmon==
{{Card Infobox DDCB-DM
 |name=Phoenixmon
 |name_jp=ホウオウモン
 |name_jp_roman=Hououmon
 |number=003
 |level=U
 |specialty=Fire
 |hp=1320
 |dp=40
 |pp=20
 |c_attack=Crimson Flame
 |c_attack_jp=スターライト{{ruby|ＥＸ|エクスプロージョン}}
 |c_attack_jp_roman=Starlight Explosion
 |c_pow=750
 |t_attack=Crimson Flare
 |t_attack_jp=クリムゾンフレア
 |t_attack_jp_roman=
 |t_pow=560
 |x_attack=Life Force
 |x_attack_jp=ライフフォース
 |x_attack_jp_roman=
 |x_pow=200
 |x_effect=Eat-Up HP
 |support=Digimon KO'd in battle revives with 500 HP. Battle is still lost.
}}
{{-}}

==004: Paildramon==
{{Card Infobox DDCB-DM
 |name=Paildramon
 |name_jp=パイルドラモン
 |name_jp_roman=
 |number=004
 |level=U
 |specialty=Fire
 |hp=1230
 |dp=30
 |pp=10
 |c_attack=Desperado Blaster
 |c_attack_jp=デスペラードブラスタ
 |c_attack_jp_roman=
 |c_pow=800
 |t_attack=Super Flash
 |t_attack_jp=エスグリーマ
 |t_attack_jp_roman=Esgrima
 |t_pow=620
 |x_attack=Electric Bolt
 |x_attack_jp=エレメンタルボルト
 |x_attack_jp_roman=Elemental Bolt
 |x_pow=450
 |x_effect={{button|x}} to 0
 |support=If own Specialty is Fire, boost own Attack Power +300.
}}
{{-}}

==005: Gigadramon==
{{Card Infobox DDCB-DM
 |name=Gigadramon
 |name_jp=ギガドラモン
 |name_jp_roman=
 |number=005
 |level=U
 |specialty=Fire
 |hp=1480
 |dp=50
 |pp=10
 |c_attack=Giga Byte Wing
 |c_attack_jp=ジェノサイドギア
 |c_attack_jp_roman=Genocide Gear
 |c_pow=900
 |t_attack=Evil Claw
 |t_attack_jp=ギルティクロー
 |t_attack_jp_roman=Guilty Claw
 |t_pow=710
 |x_attack=Giga Heat
 |x_attack_jp=ギガヒート
 |x_attack_jp_roman=
 |x_pow=550
 |x_effect=None
 |support=None
}}
{{-}}

==006: RealMetalGreymon==
{{Card Infobox DDCB-DM
 |name=RealMetalGreymon
 |name_jp=真メタルグレイモン
 |name_jp_roman=True MetalGreymon
 |number=006
 |level=U
 |specialty=Fire
 |hp=1540
 |dp=40
 |pp=10
 |c_attack=Terra Destroyer
 |c_attack_jp=テラデストロイヤー
 |c_attack_jp_roman=Tera Destroyer
 |c_pow=850
 |t_attack=Metal Slash II
 |t_attack_jp=メタルスラッシュ改
 |t_attack_jp_roman=Metal Slash Kai
 |t_pow=600
 |x_attack=Powerful Flame
 |x_attack_jp=オーヴァフレイム
 |x_attack_jp_roman=Overflame
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=Boost own Attack Power +300.
}}
{{-}}

==007: Garudamon==
{{Card Infobox DDCB-DM
 |name=Garudamon
 |name_jp=ガルダモン
 |name_jp_roman=
 |number=007
 |level=U
 |specialty=Fire
 |hp=1320
 |dp=30
 |pp=20
 |c_attack=Wing Blade
 |c_attack_jp=シャドーウイング
 |c_attack_jp_roman=Shadow Wing
 |c_pow=730
 |t_attack=Crimson Claw
 |t_attack_jp=クリムゾンクロー
 |t_attack_jp_roman=
 |t_pow=550
 |x_attack=Eagle Claw
 |x_attack_jp=イーグルクロー
 |x_attack_jp_roman=
 |x_pow=320
 |x_effect=1st Attack
 |support=If own Attack is {{button|c}}, attack first.
}}
{{-}}

==008: MasterTyrannomon==
{{Card Infobox DDCB-DM
 |name=MasterTyrannomon
 |name_jp=ティラノ師匠
 |name_jp_roman=Master Tyrano
 |number=008
 |level=U
 |specialty=Fire
 |hp=1280
 |dp=50
 |pp=20
 |c_attack=Master Fire
 |c_attack_jp=マスターファイア
 |c_attack_jp_roman=
 |c_pow=850
 |t_attack=Master Claw
 |t_attack_jp=マスタークロー
 |t_attack_jp_roman=
 |t_pow=520
 |x_attack=Hyper Heat Blast
 |x_attack_jp=超高熱闘気
 |x_attack_jp_roman=Chou Kounetsu Touki
 |x_pow=370
 |x_effect=Ice Foe x3
 |support=If own Specialty is Fire, own Attack Power is doubled.
}}
{{-}}

==009: MetalGreymon==
{{Card Infobox DDCB-DM
 |name=MetalGreymon
 |name_link=MetalGreymon (Virus)
 |name_jp=メタルグレイモン
 |name_jp_roman=
 |number=009
 |level=U
 |specialty=Fire
 |hp=1540
 |dp=30
 |pp=10
 |c_attack=Fire Blast
 |c_attack_jp=ギガデストロイヤー
 |c_attack_jp_roman=Giga Destroyer
 |c_pow=720
 |t_attack=Metal Slash
 |t_attack_jp=メタルスラッシュ
 |t_attack_jp_roman=
 |t_pow=540
 |x_attack=Flame of Fury
 |x_attack_jp=レベンジグレイム
 |x_attack_jp_roman=Revenge Flame
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=If own Level is U, boost own Attack Power +500.
}}
{{-}}

==010: Vermilimon==
{{Card Infobox DDCB-DM
 |name=Vermilimon
 |name_jp=ヴァーミリモン
 |name_jp_roman=Vermillimon
 |number=010
 |level=U
 |specialty=Fire
 |hp=1430
 |dp=30
 |pp=20
 |c_attack=Volcano Strike II
 |c_attack_jp={{ruby|ＶＣ|ヴォルケーノ}}ストライクＳ
 |c_attack_jp_roman=Volcano Strike S
 |c_pow=700
 |t_attack=Vermin Blaze
 |t_attack_jp=ヴァームブレイズ
 |t_attack_jp_roman=Verm Blaze
 |t_pow=510
 |x_attack=Hard Tackle
 |x_attack_jp=ハードタックル
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect={{button|t}} Counter
 |support=None
}}
{{-}}

==011: Meteormon==
{{Card Infobox DDCB-DM
 |name=Meteormon
 |name_jp=インセキモン
 |name_jp_roman=Insekimon
 |number=011
 |level=U
 |specialty=Fire
 |hp=1150
 |dp=30
 |pp=10
 |c_attack=Big Bang Blow
 |c_attack_jp=ビッグバンブロウ
 |c_attack_jp_roman=
 |c_pow=750
 |t_attack=Falling Star
 |t_attack_jp=フォーリンスター
 |t_attack_jp_roman=
 |t_pow=400
 |x_attack=Cosmic Flash
 |x_attack_jp=コズモフラッシュ
 |x_attack_jp_roman=
 |x_pow=200
 |x_effect={{button|c}} to 0
 |support=Lower opponent's {{button|c}} Attack Power to 0.
}}
{{-}}

==012: ExVeemon==
{{Card Infobox DDCB-DM
 |name=ExVeemon
 |name_jp=エクスブイモン
 |name_jp_roman=XV-mon
 |number=012
 |level=C
 |specialty=Fire
 |hp=810
 |dp=40
 |pp=10
 |c_attack=Ex-Laser
 |c_attack_jp=エクスレイザー
 |c_attack_jp_roman=X Laser
 |c_pow=580
 |t_attack=Power Crunch
 |t_attack_jp=ストロングクランチ
 |t_attack_jp_roman=Strong Crunch
 |t_pow=480
 |x_attack=Heart Breaker
 |x_attack_jp=ハーティシャッター
 |x_attack_jp_roman=Hearty Shatter
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=If own Level is A, boost own Attack Power +300.
}}
{{-}}

==013: Aquilamon==
{{Card Infobox DDCB-DM
 |name=Aquilamon
 |name_jp=アクィラモン
 |name_jp_roman=
 |number=013
 |level=C
 |specialty=Fire
 |hp=670
 |dp=30
 |pp=20
 |c_attack=Mach Impulse
 |c_attack_jp=マッハインプルス
 |c_attack_jp_roman=
 |c_pow=570
 |t_attack=Penetrator
 |t_attack_jp=ペネトレイター
 |t_attack_jp_roman=
 |t_pow=450
 |x_attack=Invisible Shot
 |x_attack_jp=ステルスクォーレル
 |x_attack_jp_roman=Stealth Quarrel
 |x_pow=200
 |x_effect=1st Attack
 |support=If own attack is {{button|t}}, attack first.
}}
{{-}}

==014: Greymon==
{{Card Infobox DDCB-DM
 |name=Greymon
 |name_jp=グレイモン
 |name_jp_roman=
 |number=014
 |level=C
 |specialty=Fire
 |hp=850
 |dp=40
 |pp=10
 |c_attack=Nova Blast
 |c_attack_jp=メガグレイム
 |c_attack_jp_roman=Mega Flame
 |c_pow=600
 |t_attack=Great Antler
 |t_attack_jp=グレートアントラー
 |t_attack_jp_roman=
 |t_pow=420
 |x_attack=Fire Wall
 |x_attack_jp=ファイアウォール
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=If own Level is C, boost own Attack Power +300.
}}
{{-}}

==015: Apemon==
{{Card Infobox DDCB-DM
 |name=Apemon
 |name_jp=ハヌモン
 |name_jp_roman=Hanumon
 |number=015
 |level=C
 |specialty=Fire
 |hp=830
 |dp=40
 |pp=10
 |c_attack=Angry Spike
 |c_attack_jp=怒髪天
 |c_attack_jp_roman=Dohatsuten
 |c_pow=550
 |t_attack=Bone Stick
 |t_attack_jp=如意ボーン
 |t_attack_jp_roman=Nyoi Bone
 |t_pow=420
 |x_attack=Magical Monkey Punch
 |x_attack_jp=魔猿猛爆拳
 |x_attack_jp_roman=Maen Moubakuken
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=Change own Specialty to Fire. Boost own Attack Power +200.
}}
{{-}}

==016: Tyrannomon==
{{Card Infobox DDCB-DM
 |name=Tyrannomon
 |name_jp=ティラノモン
 |name_jp_roman=Tyranomon
 |number=016
 |level=C
 |specialty=Fire
 |hp=810
 |dp=30
 |pp=20
 |c_attack=Blaze Blaster
 |c_attack_jp=ファイアーブレス
 |c_attack_jp_roman=Fire Breath
 |c_pow=520
 |t_attack=Dino Kick
 |t_attack_jp=ダイノキック
 |t_attack_jp_roman=
 |t_pow=380
 |x_attack=Wild Buster
 |x_attack_jp=ワイルドバスター
 |x_attack_jp_roman=
 |x_pow=150
 |x_effect=Nature Foe x3
 |support=None
}}
{{-}}

==017: Monochromon==
{{Card Infobox DDCB-DM
 |name=Monochromon
 |name_jp=モノクロモン
 |name_jp_roman=
 |number=017
 |level=C
 |specialty=Fire
 |hp=950
 |dp=40
 |pp=10
 |c_attack=Volcanic Strike
 |c_attack_jp={{ruby|ＶＣ|ヴォルケーノ}}ストライク
 |c_attack_jp_roman=
 |c_pow=540
 |t_attack=Big Blaze
 |t_attack_jp=グランファイアー
 |t_attack_jp_roman=Gran Fire
 |t_pow=260
 |x_attack=Guarding Tusk
 |x_attack_jp=ガーディタスク
 |x_attack_jp_roman=Guardy Tusk
 |x_pow=200
 |x_effect={{button|c}} to 0
 |support=None
}}
{{-}}

==018: Meramon==
{{Card Infobox DDCB-DM
 |name=Meramon
 |name_jp=メラモン
 |name_jp_roman=
 |number=018
 |level=C
 |specialty=Fire
 |hp=740
 |dp=30
 |pp=10
 |c_attack=Fireball
 |c_attack_jp=バーニングフィスト
 |c_attack_jp_roman=Burning Fist
 |c_pow=550
 |t_attack=Magma Bomb
 |t_attack_jp=マグマボム
 |t_attack_jp_roman=
 |t_pow=300
 |x_attack=Heat Wave
 |x_attack_jp=ヒートウェーブ
 |x_attack_jp_roman=
 |x_pow=220
 |x_effect=Ice Foe x3
 |support=If opponent's Specialty is Ice, own Attack Power is tripled.
}}
{{-}}

==019: Centarumon==
{{Card Infobox DDCB-DM
 |name=Centarumon
 |name_jp=ケンタルモン
 |name_jp_roman=Centalmon
 |number=019
 |level=C
 |specialty=Fire
 |hp=800
 |dp=40
 |pp=10
 |c_attack=Solar Ray
 |c_attack_jp=ハンティングキャノン
 |c_attack_jp_roman=Hunting Cannon
 |c_pow=450
 |t_attack=Jet Kick
 |t_attack_jp=ジェットギャロップ
 |t_attack_jp_roman=Jet Gallop
 |t_pow=360
 |x_attack=Heat Uppercut
 |x_attack_jp=ヒートアッパー
 |x_attack_jp_roman=Heat Upper
 |x_pow=220
 |x_effect=Ice Foe x3
 |support=Use {{button|c}} and Boost own {{button|c}} Attack Power +400.
}}
{{-}}

==020: Birdramon==
{{Card Infobox DDCB-DM
 |name=Birdramon
 |name_jp=バードラモン
 |name_jp_roman=
 |number=020
 |level=C
 |specialty=Fire
 |hp=710
 |dp=30
 |pp=10
 |c_attack=Meteor Wing
 |c_attack_jp=メテオウイング
 |c_attack_jp_roman=
 |c_pow=500
 |t_attack=Fire Flap
 |t_attack_jp=ファイヤーフラップ
 |t_attack_jp_roman=
 |t_pow=310
 |x_attack=Mach Grinder
 |x_attack_jp=マッハグライド
 |x_attack_jp_roman=Mach Glide
 |x_pow=130
 |x_effect=1st Attack
 |support=Attack first.
}}
{{-}}

==021: Tankmon==
{{Card Infobox DDCB-DM
 |name=Tankmon
 |name_jp=タンクモン
 |name_jp_roman=
 |number=021
 |level=C
 |specialty=Fire
 |hp=1000
 |dp=40
 |pp=10
 |c_attack=Hyper Cannon
 |c_attack_jp=ハイパーキャノン
 |c_attack_jp_roman=
 |c_pow=400
 |t_attack=Poison Drive
 |t_attack_jp=ヘルドライブ
 |t_attack_jp_roman=Hell Drive
 |t_pow=290
 |x_attack=Sub Machine Gun
 |x_attack_jp=サブバルカン
 |x_attack_jp_roman=Sub Vulcan
 |x_pow=120
 |x_effect=1st Attack
 |support=Own HP become 10. Boost own Attack Power +500.
}}
{{-}}

==022: RedVegiemon==
{{Card Infobox DDCB-DM
 |name=RedVegiemon
 |name_jp=レッドベジーモン
 |name_jp_roman=RedVagimon
 |number=022
 |level=C
 |specialty=Fire
 |hp=850
 |dp=30
 |pp=20
 |c_attack=Rotten Rainballs
 |c_attack_jp=ハザードブレス
 |c_attack_jp_roman=Hazard Breath
 |c_pow=400
 |t_attack=Red Zone
 |t_attack_jp=レッドソーン
 |t_attack_jp_roman=
 |t_pow=310
 |x_attack=Rest
 |x_attack_jp=きゅうけい
 |x_attack_jp_roman=Kyuukei
 |x_pow=0
 |x_effect=None
 |support=Discard all own DP Cards in DP Slot, boost own Attack Power +300.
}}
{{-}}

==023: Piddomon==
{{Card Infobox DDCB-DM
 |name=Piddomon
 |name_jp=ピッドモン
 |name_jp_roman=Pidmon
 |number=023
 |level=C
 |specialty=Fire
 |hp=750
 |dp=40
 |pp=20
 |c_attack=Fire Feather
 |c_attack_jp=ファイアフェザー
 |c_attack_jp_roman=
 |c_pow=450
 |t_attack=Apollo Tornado
 |t_attack_jp=アポロトルネード
 |t_attack_jp_roman=
 |t_pow=360
 |x_attack=Bit Speed
 |x_attack_jp=ピッドズピード
 |x_attack_jp_roman=Pid Speed
 |x_pow=220
 |x_effect={{button|c}} to 0
 |support=Own {{button|c}} Attack Power becomes same as own HP.
}}
{{-}}

==024: Akatorimon==
{{Card Infobox DDCB-DM
 |name=Akatorimon
 |name_jp=アカトリモン
 |name_jp_roman=
 |number=024
 |level=C
 |specialty=Fire
 |hp=600
 |dp=30
 |pp=10
 |c_attack=Chicken Red Eyes
 |c_attack_jp=スカーレットアイ
 |c_attack_jp_roman=Scarlet Eye
 |c_pow=400
 |t_attack=Dirty Attack
 |t_attack_jp=アカトリアタック
 |t_attack_jp_roman=Akatori Attack
 |t_pow=460
 |x_attack=Melting Aura
 |x_attack_jp=メルティンオーラ
 |x_attack_jp_roman=
 |x_pow=100
 |x_effect={{button|c}} to 0
 |support=Boost own Attack Power +200.
}}
{{-}}

==025: BomberNanimon==
{{Card Infobox DDCB-DM
 |name=BomberNanimon
 |name_jp=ボンバーナニモン
 |name_jp_roman=
 |number=025
 |level=C
 |specialty=Fire
 |hp=650
 |dp=30
 |pp=10
 |c_attack=Free Throw Bomb
 |c_attack_jp=フリースローボム
 |c_attack_jp_roman=
 |c_pow=520
 |t_attack=K.O. Punch
 |t_attack_jp=爆・オヤジパンチ
 |t_attack_jp_roman=Baku Oyaji Punch
 |t_pow=390
 |x_attack=Count Down
 |x_attack_jp=カウントダウン
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect=Crash
 |support=If both Levels are C, boost own Attack Power +400.
}}
{{-}}

==026: Flarerizamon==
{{Card Infobox DDCB-DM
 |name=Flarerizamon
 |name_jp=フレアリザモン
 |name_jp_roman=FlareLizamon
 |number=026
 |level=C
 |specialty=Fire
 |hp=730
 |dp=20
 |pp=10
 |c_attack=Blaze Buster
 |c_attack_jp=フレイムヒット
 |c_attack_jp_roman=Flame Hit
 |c_pow=550
 |t_attack=Tower of Fire
 |t_attack_jp=ファイアータワー
 |t_attack_jp_roman=Fire Tower
 |t_pow=320
 |x_attack=Thrusting Rush
 |x_attack_jp=スラストラッシュ
 |x_attack_jp_roman=Thrust Rush
 |x_pow=240
 |x_effect=None
 |support=Change own Specialty to Fire.
}}
{{-}}

==027: Agumon==
{{Card Infobox DDCB-DM
 |name=Agumon
 |name_jp=アグモン
 |name_jp_roman=
 |number=027
 |level=R
 |specialty=Fire
 |hp=570
 |dp=0
 |pp=20
 |c_attack=Pepper Breath
 |c_attack_jp=ベビーフレイム
 |c_attack_jp_roman=Baby Flame
 |c_pow=380
 |t_attack=Spirit Fire
 |t_attack_jp=スピットファイア
 |t_attack_jp_roman=Spitfire
 |t_pow=200
 |x_attack=Cross Fire
 |x_attack_jp=クロスファイト
 |x_attack_jp_roman=Cross Fight
 |x_pow=120
 |x_effect={{button|c}} to 0
 |support=Boost own {{button|c}} Attack Power +300.
}}
{{-}}

==028: Solarmon==
{{Card Infobox DDCB-DM
 |name=Solarmon
 |name_jp=ソーラーモン
 |name_jp_roman=
 |number=028
 |level=R
 |specialty=Fire
 |hp=500
 |dp=0
 |pp=20
 |c_attack=Solar Flare
 |c_attack_jp=シャイニーリング
 |c_attack_jp_roman=Shiny Ring
 |c_pow=350
 |t_attack=Soul Shocker
 |t_attack_jp=ソルカロール
 |t_attack_jp_roman=Sol Calor
 |t_pow=210
 |x_attack=Little Burn
 |x_attack_jp=リトルバーン
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect=Crash
 |support=None
}}
{{-}}

==029: Biyomon==
{{Card Infobox DDCB-DM
 |name=Biyomon
 |name_jp=ピヨモン
 |name_jp_roman=Piyomon
 |number=029
 |level=R
 |specialty=Fire
 |hp=510
 |dp=0
 |pp=20
 |c_attack=Spiral Twister
 |c_attack_jp=マジカルファイアー
 |c_attack_jp_roman=Magical Fire
 |c_pow=350
 |t_attack=Violin Attack
 |t_attack_jp=ピヨリンアタック
 |t_attack_jp_roman=Piyorin Attack
 |t_pow=170
 |x_attack=Turbo Pecker
 |x_attack_jp=ダッシュついばみ
 |x_attack_jp_roman=Dash Tsuibami
 |x_pow=130
 |x_effect=1st Attack
 |support=Boost own Attack Power +200.
}}
{{-}}

==030: Muchomon==
{{Card Infobox DDCB-DM
 |name=Muchomon
 |name_jp=ムーチョモン
 |name_jp_roman=
 |number=030
 |level=R
 |specialty=Fire
 |hp=600
 |dp=0
 |pp=20
 |c_attack=Tropical Beak
 |c_attack_jp=トロピカルビーク
 |c_attack_jp_roman=
 |c_pow=320
 |t_attack=Red Hot Flare
 |t_attack_jp=アーデントフレア
 |t_attack_jp_roman=Ardent Flare
 |t_pow=220
 |x_attack=Counter Step
 |x_attack_jp=カウンタービンタ
 |x_attack_jp_roman=Counter Binta
 |x_pow=0
 |x_effect={{button|x}} Counter
 |support=Boost own {{button|t}} Attack Power +300.
}}
{{-}}

==031: Candlemon==
{{Card Infobox DDCB-DM
 |name=Candlemon
 |name_jp=キャンドモン
 |name_jp_roman=Candmon
 |number=031
 |level=R
 |specialty=Fire
 |hp=480
 |dp=0
 |pp=20
 |c_attack=Flame Bomber
 |c_attack_jp=ボンファイア
 |c_attack_jp_roman=Bonfire
 |c_pow=380
 |t_attack=Molten Wax
 |t_attack_jp=メルトワックス
 |t_attack_jp_roman=Melt Wax
 |t_pow=270
 |x_attack=Karmic Flame
 |x_attack_jp=カルマフレイマー
 |x_attack_jp_roman=Karma Flamer
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=Boost own {{button|x}} Attack Power +200.
}}
{{-}}

==032: D-Otamamon==
{{Card Infobox DDCB-DM
 |name=D-Otamamon
 |name_jp=オタマモンD
 |name_jp_roman=Otamamon D
 |number=032
 |level=R
 |specialty=Fire
 |hp=550
 |dp=0
 |pp=20
 |c_attack=Boiling Bubble
 |c_attack_jp=ボイルドバブル
 |c_attack_jp_roman=
 |c_pow=300
 |t_attack=Rover Claw
 |t_attack_jp=ラヴァクロー
 |t_attack_jp_roman=Lava Claw
 |t_pow=200
 |x_attack=Magma Stream
 |x_attack_jp=マグマドリップ
 |x_attack_jp_roman=Magma Drip
 |x_pow=150
 |x_effect=Ice Foe x3.
 |support=If opponent's Specialty is Ice, own Attack Power is doubled.
}}
{{-}}

==033: Goburimon==
{{Card Infobox DDCB-DM
 |name=Goburimon
 |name_jp=ゴブリモン
 |name_jp_roman=
 |number=033
 |level=R
 |specialty=Fire
 |hp=500
 |dp=0
 |pp=20
 |c_attack=Goburi Bomb
 |c_attack_jp=ゴブリボム
 |c_attack_jp_roman=
 |c_pow=300
 |t_attack=Goburi Strike
 |t_attack_jp=ゴブリストライク
 |t_attack_jp_roman=
 |t_pow=300
 |x_attack=Goburi Rush
 |x_attack_jp=ゴブリラッシュ
 |x_attack_jp_roman=
 |x_pow=300
 |x_effect=None
 |support=None
}}
{{-}}

==034: Vikemon==
{{Card Infobox DDCB-DM
 |name=Vikemon
 |name_jp=ヴァイクモン
 |name_jp_roman=
 |number=034
 |level=U
 |specialty=Ice
 |hp=2420
 |dp=50
 |pp=10
 |c_attack=Artic Blizzard
 |c_attack_jp={{ruby|ＡＲＣ|アークティック}}ブリザード
 |c_attack_jp_roman=
 |c_pow=760
 |t_attack=Viking Flare
 |t_attack_jp=ヴァイキングフレイル
 |t_attack_jp_roman=Viking Flail
 |t_pow=570
 |x_attack=Bazzoka Howl
 |x_attack_jp=バーサークハウル
 |x_attack_jp_roman=Berserk Howl
 |x_pow=390
 |x_effect={{button|c}} to 0
 |support=None
}}
{{-}}

==035: Omnimon II==
{{Card Infobox DDCB-DM
 |name=Omnimon II
 |name_link=Omnimon
 |name_jp=オメガモンII
 |name_jp_roman=Omegamon II
 |number=035
 |level=U
 |specialty=Ice
 |hp=2420
 |dp=60
 |pp=10
 |c_attack=Transcendent Sword
 |c_attack_jp=グレイソード
 |c_attack_jp_roman=Grey Sword
 |c_pow=550
 |t_attack=Garuru Cannon
 |t_attack_jp=ガルルキャノン
 |t_attack_jp_roman=
 |t_pow=800
 |x_attack=Double Shot
 |x_attack_jp=ダブルトレント
 |x_attack_jp_roman=Double Torrent
 |x_pow=0
 |x_effect={{button|x}} Counter
 |support=Change own Specialty to Ice. Recover own HP by +100.
}}
{{-}}

==036: MetalSeadramon==
{{Card Infobox DDCB-DM
 |name=MetalSeadramon
 |name_jp=メタルシードラモン
 |name_jp_roman=
 |number=036
 |level=U
 |specialty=Ice
 |hp=2030
 |dp=50
 |pp=20
 |c_attack=River of Power
 |c_attack_jp={{ruby|ＵＬＴ|アルティメント}}ストリーム
 |c_attack_jp_roman=Ultimate Stream
 |c_pow=700
 |t_attack=Hot Squeeze
 |t_attack_jp=ヘルズクイーズ
 |t_attack_jp_roman=Hell Squeeze
 |t_pow=450
 |x_attack=Poseidon's Divide
 |x_attack_jp=ポセイドンディバイド
 |x_attack_jp_roman=Poseidon Divide
 |x_pow=400
 |x_effect=Fire Foe x3
 |support=If own Specialty is Ice, opponent's Support Effect is voided.
}}
{{-}}

==037: MetalGarurumon==
{{Card Infobox DDCB-DM
 |name=MetalGarurumon
 |name_jp=メタルガルルモン
 |name_jp_roman=
 |number=037
 |level=U
 |specialty=Ice
 |hp=2250
 |dp=50
 |pp=20
 |c_attack=Metal Wolf Claw
 |c_attack_jp=コキュートスブレス
 |c_attack_jp_roman=Cocytus Breath
 |c_pow=700
 |t_attack=Garuru Tomahawk
 |t_attack_jp=ガルルトマホーク
 |t_attack_jp_roman=
 |t_pow=450
 |x_attack=Giga Cross Freezer
 |x_attack_jp={{ruby|Ｇ|グランド}}クロスフリーザー
 |x_attack_jp_roman=Grand Cross Freeze
 |x_pow=400
 |x_effect=Fire Foe x3
 |support=If own Cards in Hand 3 or more, opponent's Attack Power becomes 0.
}}
{{-}}

==038: MarineAngemon==
{{Card Infobox DDCB-DM
 |name=MarineAngemon
 |name_jp=マリンエンジェモン
 |name_jp_roman=MarinAngemon
 |number=038
 |level=U
 |specialty=Ice
 |hp=1540
 |dp=30
 |pp=20
 |c_attack=Ocean Love
 |c_attack_jp=オーシャンラブ
 |c_attack_jp_roman=
 |c_pow=630
 |t_attack=Marine Shot
 |t_attack_jp=マリンスコードロン
 |t_attack_jp_roman=Marine Squadron
 |t_pow=480
 |x_attack=Extra Smile
 |x_attack_jp=エクストラスマイル
 |x_attack_jp_roman=
 |x_pow=220
 |x_effect={{button|c}} to 0
 |support=Recover own HP by +200.
}}
{{-}}

==039: WereGarurumon==
{{Card Infobox DDCB-DM
 |name=WereGarurumon
 |name_jp=ワーガルルモン
 |name_jp_roman=
 |number=039
 |level=U
 |specialty=Ice
 |hp=1820
 |dp=30
 |pp=20
 |c_attack=Wolf Claw
 |c_attack_jp=カイザーネイル
 |c_attack_jp_roman=Kaiser Nail
 |c_pow=670
 |t_attack=Blow Hard
 |t_attack_jp=ボールディブロー
 |t_attack_jp_roman=Baldy Blow
 |t_pow=500
 |x_attack=Moonsault Kick
 |x_attack_jp=円月蹴り
 |x_attack_jp_roman=Engetsugeri
 |x_pow=0
 |x_effect={{button|t}} Counter
 |support=Add number of DP Cards in DP Slot x100 to own HP.
}}
{{-}}

==040: Zudomon==
{{Card Infobox DDCB-DM
 |name=Zudomon
 |name_jp=ズドモン
 |name_jp_roman=
 |number=040
 |level=U
 |specialty=Ice
 |hp=2090
 |dp=40
 |pp=20
 |c_attack=Vulcan's Hammer
 |c_attack_jp=ハンマースパーク
 |c_attack_jp_roman=Hammer Spark
 |c_pow=700
 |t_attack=Horn & Tusk
 |t_attack_jp=ホルン＆タスク
 |t_attack_jp_roman=
 |t_pow=300
 |x_attack=Cold Crusher
 |x_attack_jp=アイスロードバンプ
 |x_attack_jp_roman=Ice Road Bump
 |x_pow=250
 |x_effect={{button|c}} to 0
 |support=If own Specialty is Ice, opponent's Attack Power is halved.
}}
{{-}}

==041: Panjyamon==
{{Card Infobox DDCB-DM
 |name=Panjyamon
 |name_jp=パンジャモン
 |name_jp_roman=
 |number=041
 |level=U
 |specialty=Ice
 |hp=1800
 |dp=30
 |pp=20
 |c_attack=The Fist of Ice
 |c_attack_jp=氷獣拳
 |c_attack_jp_roman=Hyoujuuken
 |c_pow=620
 |t_attack=Frozen Shockwave
 |t_attack_jp=冷気功
 |t_attack_jp_roman=Reikikou
 |t_pow=390
 |x_attack=Shadow Spin Kick
 |x_attack_jp=残影反転撃
 |x_attack_jp_roman=Zan'ei Hantengeki
 |x_pow=0
 |x_effect={{button|t}} Counter
 |support={{button|t}} Counterattack. Attack second.
}}
{{-}}

==042: MegaSeadramon==
{{Card Infobox DDCB-DM
 |name=MegaSeadramon
 |name_jp=メガシードラモン
 |name_jp_roman=
 |number=042
 |level=U
 |specialty=Ice
 |hp=1870
 |dp=40
 |pp=20
 |c_attack=Mail Storm
 |c_attack_jp=メイルストローム
 |c_attack_jp_roman=Maelstrom
 |c_pow=650
 |t_attack=Lightning Javelin
 |t_attack_jp=サンダージャベリン
 |t_attack_jp_roman=Thunder Javelin
 |t_pow=360
 |x_attack=Ice Reflector
 |x_attack_jp=アイスリフレクト
 |x_attack_jp_roman=Ice Reflect
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support={{button|c}} Counterattack. Attack second.
}}
{{-}}

==043: WaruSeadramon==
{{Card Infobox DDCB-DM
 |name=WaruSeadramon
 |name_jp=ワルシードラモン
 |name_jp_roman=
 |number=043
 |level=U
 |specialty=Ice
 |hp=1760
 |dp=40
 |pp=10
 |c_attack=Dark Blast
 |c_attack_jp=ダークストローム
 |c_attack_jp_roman=Darkstrom
 |c_pow=650
 |t_attack=Evil Icicle
 |t_attack_jp=イビルアイシクル
 |t_attack_jp_roman=
 |t_pow=360
 |x_attack=Strange Mist
 |x_attack_jp=ストレンジミスト
 |x_attack_jp_roman=
 |x_pow=200
 |x_effect=Jamming
 |support=Opponent's Support Effect is voided.
}}
{{-}}

==044: Brachiomon==
{{Card Infobox DDCB-DM
 |name=Brachiomon
 |name_jp=ブラキモン
 |name_jp_roman=
 |number=044
 |level=U
 |specialty=Ice
 |hp=2300
 |dp=30
 |pp=20
 |c_attack=Brachio Bubble
 |c_attack_jp=ブラキオバブル
 |c_attack_jp_roman=
 |c_pow=600
 |t_attack=Hammerhead
 |t_attack_jp=ハンマーヘッド
 |t_attack_jp_roman=
 |t_pow=380
 |x_attack=Aqua Shatter
 |x_attack_jp=アクアシャッター
 |x_attack_jp_roman=
 |x_pow=150
 |x_effect={{button|c}} to 0
 |support=Lower opponent's {{button|c}} Attack Power to 0.
}}
{{-}}

==045: BlueMeramon==
{{Card Infobox DDCB-DM
 |name=BlueMeramon
 |name_jp=ブルーメラモン
 |name_jp_roman=
 |number=045
 |level=U
 |specialty=Ice
 |hp=1430
 |dp=30
 |pp=10
 |c_attack=Ice Phantom
 |c_attack_jp=アイスファントム
 |c_attack_jp_roman=
 |c_pow=700
 |t_attack=Cold Flame
 |t_attack_jp=コールドフレイム
 |t_attack_jp_roman=
 |t_pow=480
 |x_attack=Vision Blinder
 |x_attack_jp=ビジョンバインド
 |x_attack_jp_roman=Vision Bind
 |x_pow=360
 |x_effect={{button|x}} to 0
 |support=Lower opponent's {{button|x}} Attack Power to 0.
}}
{{-}}

==046: Garurumon==
{{Card Infobox DDCB-DM
 |name=Garurumon
 |name_jp=ガルルモン
 |name_jp_roman=
 |number=046
 |level=C
 |specialty=Ice
 |hp=1100
 |dp=30
 |pp=10
 |c_attack=Howling Blaster
 |c_attack_jp=フォクスファイアー
 |c_attack_jp_roman=Fox Fire
 |c_pow=350
 |t_attack=Subzero Ice Fang
 |t_attack_jp=フリーズファング
 |t_attack_jp_roman=Freeze Fang
 |t_pow=230
 |x_attack=Ice Wall
 |x_attack_jp=アイスウォール
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=Opponent uses {{button|c}}.
}}
{{-}}

==047: Ikkakumon==
{{Card Infobox DDCB-DM
 |name=Ikkakumon
 |name_jp=イッカクモン
 |name_jp_roman=
 |number=047
 |level=C
 |specialty=Ice
 |hp=1200
 |dp=40
 |pp=20
 |c_attack=Harpoon Torpedo
 |c_attack_jp=ハープーンバルカン
 |c_attack_jp_roman=Harpoon Vulcan
 |c_pow=340
 |t_attack=Heat Top
 |t_attack_jp=ヒートトップ
 |t_attack_jp_roman=
 |t_pow=250
 |x_attack=Northen Light
 |x_attack_jp=ノーザンライツ
 |x_attack_jp_roman=Northern Lights
 |x_pow=200
 |x_effect=Fire Foe x3
 |support=If opponent's Specialty is Fire, own Attack Power is tripled.
}}
{{-}}

==048: Dolphmon==
{{Card Infobox DDCB-DM
 |name=Dolphmon
 |name_jp=ルカモン
 |name_jp_roman=Rukamon
 |number=048
 |level=C
 |specialty=Ice
 |hp=1000
 |dp=40
 |pp=20
 |c_attack=Pulse Blast
 |c_attack_jp=シェイキングパルス
 |c_attack_jp_roman=Shaking Pulse
 |c_pow=330
 |t_attack=Dolphin Kick
 |t_attack_jp=ドルフィンキック
 |t_attack_jp_roman=
 |t_pow=290
 |x_attack=Blast Away
 |x_attack_jp=ボン・ヴォヤージュ
 |x_attack_jp_roman=Bon Voyage
 |x_pow=200
 |x_effect={{button|x}} to 0
 |support=If own Attack is not {{button|c}}, recover own HP by +300.
}}
{{-}}

==049: Whamon==
{{Card Infobox DDCB-DM
 |name=Whamon
 |name_link=Whamon (Champion)
 |name_jp=ホエーモン
 |name_jp_roman=
 |number=049
 |level=C
 |specialty=Ice
 |hp=1300
 |dp=40
 |pp=20
 |c_attack=Tidal Wave
 |c_attack_jp=タイダルウェーブ
 |c_attack_jp_roman=
 |c_pow=340
 |t_attack=Jet Arrow
 |t_attack_jp=ジェットアロー
 |t_attack_jp_roman=
 |t_pow=220
 |x_attack=Giant Press
 |x_attack_jp=ギガントプレス
 |x_attack_jp_roman=Gigant Press
 |x_pow=150
 |x_effect={{button|t}} to 0
 |support=Own HP become 700.
}}
{{-}}

==050: Seadramon==
{{Card Infobox DDCB-DM
 |name=Seadramon
 |name_jp=シードラモン
 |name_jp_roman=
 |number=050
 |level=C
 |specialty=Ice
 |hp=1150
 |dp=40
 |pp=20
 |c_attack=Ice Blast
 |c_attack_jp=アイスアロー
 |c_attack_jp_roman=Ice Arrow
 |c_pow=360
 |t_attack=Water Shock
 |t_attack_jp=ウォーターブレス
 |t_attack_jp_roman=Water Breath
 |t_pow=250
 |x_attack=Mind Freezer
 |x_attack_jp=チルブレインズ
 |x_attack_jp_roman=Chill Brains
 |x_pow=100
 |x_effect={{button|c}} to 0
 |support=Opponent's Attack Power is halved.
}}
{{-}}

==051: Gesomon==
{{Card Infobox DDCB-DM
 |name=Gesomon
 |name_jp=ゲソモン
 |name_jp_roman=
 |number=051
 |level=C
 |specialty=Ice
 |hp=1030
 |dp=30
 |pp=10
 |c_attack=Coral Crusher
 |c_attack_jp=デッドリーシェイド
 |c_attack_jp_roman=Deadly Shade
 |c_pow=400
 |t_attack=Evil Punch
 |t_attack_jp=デビルバッシング
 |t_attack_jp_roman=Devil Bashing
 |t_pow=250
 |x_attack=Knight's Dome
 |x_attack_jp=スクワイアドーム
 |x_attack_jp_roman=Squire Dome
 |x_pow=160
 |x_effect={{button|c}} to 0
 |support=None
}}
{{-}}

==052: Frigimon==
{{Card Infobox DDCB-DM
 |name=Frigimon
 |name_jp=ユキダルモン
 |name_jp_roman=Yukidarumon
 |number=052
 |level=C
 |specialty=Ice
 |hp=990
 |dp=30
 |pp=20
 |c_attack=Subzero Ice Punch
 |c_attack_jp=絶対零度パンチ
 |c_attack_jp_roman=Zettai Reido Punch
 |c_pow=350
 |t_attack=Icy Breath
 |t_attack_jp=アイスブレス
 |t_attack_jp_roman=Ice Breath
 |t_pow=200
 |x_attack=Snowball
 |x_attack_jp=雪合戦
 |x_attack_jp_roman=Yukigassen
 |x_pow=170
 |x_effect=Fire Foe x3
 |support=Recover own HP by +200.
}}
{{-}}

==053: Gekomon==
{{Card Infobox DDCB-DM
 |name=Gekomon
 |name_jp=ゲコモン
 |name_jp_roman=
 |number=053
 |level=C
 |specialty=Ice
 |hp=960
 |dp=30
 |pp=20
 |c_attack=Symphony Crusher
 |c_attack_jp={{ruby|Ｃ|クラッシュ}}シンゴニー
 |c_attack_jp_roman=Crush Symphony
 |c_pow=340
 |t_attack=Noisy Echo
 |t_attack_jp=ノイジーエコー
 |t_attack_jp_roman=
 |t_pow=220
 |x_attack=Frog Jump
 |x_attack_jp=フロッグジャンプ
 |x_attack_jp_roman=
 |x_pow=100
 |x_effect={{button|c}} to 0
 |support=Change opponent's Specialty to Ice.
}}
{{-}}

==054: Coelamon==
{{Card Infobox DDCB-DM
 |name=Coelamon
 |name_jp=シーラモン
 |name_jp_roman=
 |number=054
 |level=C
 |specialty=Ice
 |hp=1270
 |dp=50
 |pp=10
 |c_attack=Fossil Bite
 |c_attack_jp=ヴァリアブルダーツ
 |c_attack_jp_roman=Variable Darts
 |c_pow=400
 |t_attack=Water Brick
 |t_attack_jp=ウォータブリット
 |t_attack_jp_roman=Water Bullet
 |t_pow=290
 |x_attack=Iron Scale
 |x_attack_jp=アイアンスケイル
 |x_attack_jp_roman=
 |x_pow=210
 |x_effect={{button|c}} to 0
 |support=Lower opponent's {{button|c}} Attack Power to 0.
}}
{{-}}

==055: Mojyamon==
{{Card Infobox DDCB-DM
 |name=Mojyamon
 |name_jp=モジャモン
 |name_jp_roman=
 |number=055
 |level=C
 |specialty=Ice
 |hp=980
 |dp=30
 |pp=20
 |c_attack=Icicle Fire
 |c_attack_jp=アイスクルロッド
 |c_attack_jp_roman=Icicle Rod
 |c_pow=370
 |t_attack=Bone Boomerang
 |t_attack_jp=骨骨ブーメラン
 |t_attack_jp_roman=Honehone Boomerang
 |t_pow=290
 |x_attack=Dancing Punch
 |x_attack_jp=ダンシングパンチ
 |x_attack_jp_roman=
 |x_pow=210
 |x_effect=None
 |support=Recover own HP by +200.
}}
{{-}}

==056: Shellmon==
{{Card Infobox DDCB-DM
 |name=Shellmon
 |name_jp=シェルモン
 |name_jp_roman=
 |number=056
 |level=C
 |specialty=Ice
 |hp=1250
 |dp=30
 |pp=10
 |c_attack=Hydro Blaster
 |c_attack_jp=ハイドロプレッシャー
 |c_attack_jp_roman=Hydro Pressure
 |c_pow=340
 |t_attack=Drill Shell
 |t_attack_jp=ドリルシェル
 |t_attack_jp_roman=
 |t_pow=200
 |x_attack=Spin Shatter
 |x_attack_jp=スピンシェルター
 |x_attack_jp_roman=Spin Shelter
 |x_pow=150
 |x_effect={{button|c}} to 0
 |support=If opponent used {{button|c}}, change it to {{button|x}}.
}}
{{-}}

==057: Sorcerimon==
{{Card Infobox DDCB-DM
 |name=Sorcerimon
 |name_jp=ソーサリモン
 |name_jp_roman=
 |number=057
 |level=C
 |specialty=Ice
 |hp=900
 |dp=40
 |pp=10
 |c_attack=Crystal Cloud
 |c_attack_jp=クリスタルクラウド
 |c_attack_jp_roman=
 |c_pow=440
 |t_attack=Drowning Aquarius
 |t_attack_jp=アクエリアスフィル
 |t_attack_jp_roman=Aquarius Fill
 |t_pow=370
 |x_attack=Ice Illusion
 |x_attack_jp=アイスイリュージョン
 |x_attack_jp_roman=
 |x_pow=170
 |x_effect=Jamming
 |support=Change own Specialty to Ice.
}}
{{-}}

==058: IceDevimon==
{{Card Infobox DDCB-DM
 |name=IceDevimon
 |name_jp=アイスデビモン
 |name_jp_roman=
 |number=058
 |level=C
 |specialty=Ice
 |hp=990
 |dp=40
 |pp=10
 |c_attack=Frost Claw
 |c_attack_jp=フロストクロー
 |c_attack_jp_roman=
 |c_pow=390
 |t_attack=Icy Shower
 |t_attack_jp=アイシーシャワー
 |t_attack_jp_roman=
 |t_pow=290
 |x_attack=Sub Zero Freeze
 |x_attack_jp=ゼロフリーズ
 |x_attack_jp_roman=Zero Freeze
 |x_pow=180
 |x_effect=Fire Foe x3
 |support=If opponent's Specialty is fire, own Attack Power is tripled.
}}
{{-}}

==059: Hyogamon==
{{Card Infobox DDCB-DM
 |name=Hyogamon
 |name_jp=ヒョーガモン
 |name_jp_roman=Hyougamon
 |number=059
 |level=C
 |specialty=Ice
 |hp=1200
 |dp=40
 |pp=10
 |c_attack=Icy Cudgel
 |c_attack_jp=氷丸投げ
 |c_attack_jp_roman=Hyougan Nage
 |c_pow=460
 |t_attack=Ice Mace
 |t_attack_jp=アイスこん棒
 |t_attack_jp_roman=Ice Konbou
 |t_pow=250
 |x_attack=Snow Barrier
 |x_attack_jp=スノーバリア
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=None
}}
{{-}}

==060: Icemon==
{{Card Infobox DDCB-DM
 |name=Icemon
 |name_jp=アイスモン
 |name_jp_roman=
 |number=060
 |level=C
 |specialty=Ice
 |hp=1140
 |dp=30
 |pp=20
 |c_attack=Iceball Bomb
 |c_attack_jp=アイスボールボム
 |c_attack_jp_roman=
 |c_pow=370
 |t_attack=Ice Block
 |t_attack_jp=オンザロック
 |t_attack_jp_roman=On the Rock
 |t_pow=240
 |x_attack=Ice Strike
 |x_attack_jp=アイスストライク
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect={{button|x}} Counter
 |support=None
}}
{{-}}

==061: Gomamon==
{{Card Infobox DDCB-DM
 |name=Gomamon
 |name_jp=ゴマモン
 |name_jp_roman=
 |number=061
 |level=R
 |specialty=Ice
 |hp=700
 |dp=0
 |pp=20
 |c_attack=Marching Fishes
 |c_attack_jp={{ruby|Ｍ|マーティング}}フィッシーズ
 |c_attack_jp_roman=
 |c_pow=300
 |t_attack=Sharp Edge
 |t_attack_jp=シャープエッジ
 |t_attack_jp_roman=
 |t_pow=240
 |x_attack=Big Wave Attack
 |x_attack_jp=サーファーダイブ
 |x_attack_jp_roman=Surfer Dive
 |x_pow=200
 |x_effect={{button|t}} to 0
 |support=Lower opponent's {{button|t}} Attack Power to 0.
}}
{{-}}

==062: Gabumon==
{{Card Infobox DDCB-DM
 |name=Gabumon
 |name_jp=ガブモン
 |name_jp_roman=
 |number=062
 |level=R
 |specialty=Ice
 |hp=680
 |dp=0
 |pp=20
 |c_attack=Blue Blaster
 |c_attack_jp=プチファイアー
 |c_attack_jp_roman=Petit Fire
 |c_pow=350
 |t_attack=Little Horn
 |t_attack_jp=リトルホーン
 |t_attack_jp_roman=
 |t_pow=220
 |x_attack=Hidden Punch
 |x_attack_jp=ヒドゥンノーク
 |x_attack_jp_roman=Hidden Knock
 |x_pow=140
 |x_effect={{button|c}} to 0
 |support=None
}}
{{-}}

==063: Betamon==
{{Card Infobox DDCB-DM
 |name=Betamon
 |name_jp=ベタモン
 |name_jp_roman=
 |number=063
 |level=R
 |specialty=Ice
 |hp=730
 |dp=0
 |pp=20
 |c_attack=Electric Shock
 |c_attack_jp=電撃ビリリン
 |c_attack_jp_roman=Dengeki Biririn
 |c_pow=300
 |t_attack=Fin Cutter
 |t_attack_jp=カッターフィン
 |t_attack_jp_roman=Cutter Fin
 |t_pow=190
 |x_attack=Water Tower
 |x_attack_jp=ウォータータワー
 |x_attack_jp_roman=
 |x_pow=170
 |x_effect={{button|c}} to 0
 |support=If own HP are less then 200, reduce opponent's Attack Power to 0.
}}
{{-}}

==064: Penguinmon==
{{Card Infobox DDCB-DM
 |name=Penguinmon
 |name_jp=ペンモン
 |name_jp_roman=Penmon
 |number=064
 |level=R
 |specialty=Ice
 |hp=670
 |dp=0
 |pp=20
 |c_attack=Eternal Slapping
 |c_attack_jp=無限ビンタ
 |c_attack_jp_roman=Mugen Binta
 |c_pow=320
 |t_attack=Sliding Attack
 |t_attack_jp=スライドアタック
 |t_attack_jp_roman=Slide Attack
 |t_pow=180
 |x_attack=Ice Prism
 |x_attack_jp=アイスブリズム
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect={{button|c}} to 0
 |support=If opponent's Specialty is Fire, reduce opponent's Attack Power to 0.
}}
{{-}}

==065: Gizamon==
{{Card Infobox DDCB-DM
 |name=Gizamon
 |name_jp=ギザモン
 |name_jp_roman=
 |number=065
 |level=R
 |specialty=Ice
 |hp=650
 |dp=0
 |pp=20
 |c_attack=Spiral Saw
 |c_attack_jp=スパイラルエッジ
 |c_attack_jp_roman=Spiral Edge
 |c_pow=260
 |t_attack=Frog Kick
 |t_attack_jp=フロッグキック
 |t_attack_jp_roman=
 |t_pow=200
 |x_attack=Water Cure
 |x_attack_jp=ウォーターキュア
 |x_attack_jp_roman=
 |x_pow=150
 |x_effect=Fire Foe x3
 |support=If opponent's Specialty is Fire, own Attack Power is doubled.
}}
{{-}}

==066: Otamamon==
{{Card Infobox DDCB-DM
 |name=Otamamon
 |name_jp=オタマモン
 |name_jp_roman=
 |number=066
 |level=R
 |specialty=Ice
 |hp=710
 |dp=0
 |pp=20
 |c_attack=Stun Bubble
 |c_attack_jp=ララバイバブル
 |c_attack_jp_roman=Lullaby Bubble
 |c_pow=330
 |t_attack=Kid Claw
 |t_attack_jp=チャイルドクロー
 |t_attack_jp_roman=Child Claw
 |t_pow=130
 |x_attack=Wrapping Bubble
 |x_attack_jp=ラッピングバブル
 |x_attack_jp_roman=
 |x_pow=100
 |x_effect={{button|c}} to 0
 |support=Reduce opponent's {{button|c}} Attack Power to 0.
}}
{{-}}

==067: SnowAgumon==
{{Card Infobox DDCB-DM
 |name=SnowAgumon
 |name_jp=ユキアグモン
 |name_jp_roman=YukiAgumon
 |number=067
 |level=R
 |specialty=Ice
 |hp=720
 |dp=0
 |pp=20
 |c_attack=Hail Storm
 |c_attack_jp=ホワイトヘイル
 |c_attack_jp_roman=White Hail
 |c_pow=160
 |t_attack=Little Blizzard
 |t_attack_jp=リトルブリザード
 |t_attack_jp_roman=
 |t_pow=200
 |x_attack=Freeze Beam
 |x_attack_jp=アイスカムカム
 |x_attack_jp_roman=Ice Kamukamu
 |x_pow=220
 |x_effect={{button|x}} to 0
 |support=Reduce opponent's {{button|x}} Attack Power to 0.
}}
{{-}}

==068: SnowGoburimon==
{{Card Infobox DDCB-DM
 |name=SnowGoburimon
 |name_jp=スノーゴブリモン
 |name_jp_roman=
 |number=068
 |level=R
 |specialty=Ice
 |hp=770
 |dp=0
 |pp=20
 |c_attack=Bolt Strike
 |c_attack_jp=スノーゴブボルト
 |c_attack_jp_roman=SnowGobu Bolt
 |c_pow=230
 |t_attack=Snow Gobu Mace
 |t_attack_jp=スノーゴブこん棒
 |t_attack_jp_roman=SnowGobu Konbou
 |t_pow=230
 |x_attack=Freezing Gobu Breath
 |x_attack_jp=スノーゴブブレス
 |x_attack_jp_roman=SnowGobu Breath
 |x_pow=230
 |x_effect=None
 |support=None
}}
{{-}}

==069: Valkyrimon==
{{Card Infobox DDCB-DM
 |name=Valkyrimon
 |name_jp=ヴァルキリモン
 |name_jp_roman=
 |number=069
 |level=U
 |specialty=Nature
 |hp=1590
 |dp=50
 |pp=20
 |c_attack=Feral Sword
 |c_attack_jp=フェンリルソード
 |c_attack_jp_roman=Fenrir Sword
 |c_pow=840
 |t_attack=Laser Javelin
 |t_attack_jp=レーザージャベリン
 |t_attack_jp_roman=
 |t_pow=550
 |x_attack=Punishing Storm
 |x_attack_jp=サンクションストーム
 |x_attack_jp_roman=Sanction Storm
 |x_pow=350
 |x_effect={{button|c}} to 0
 |support=Opponent uses O.
}}
{{-}}

==070: Seraphimon==
{{Card Infobox DDCB-DM
 |name=Seraphimon
 |name_jp=セラフィモン
 |name_jp_roman=
 |number=070
 |level=U
 |specialty=Nature
 |hp=1650
 |dp=50
 |pp=20
 |c_attack=Seventh Heaven
 |c_attack_jp=セブンヘブンズ
 |c_attack_jp_roman=Seven Heavens
 |c_pow=900
 |t_attack=Rising Halo
 |t_attack_jp=アセンションハーロー
 |t_attack_jp_roman=Ascension Hallow
 |t_pow=510
 |x_attack=Divine Breaker
 |x_attack_jp=ディバインブレーカー
 |x_attack_jp_roman=
 |x_pow=420
 |x_effect=Dark Foe x3
 |support=If opponent's Specialty is Darkness, own Attack Power is +200 & HP +200.
}}
{{-}}

==071: Magnadramon==
{{Card Infobox DDCB-DM
 |name=Magnadramon
 |name_jp=ホーリードラモン
 |name_jp_roman=
 |number=071
 |level=U
 |specialty=Nature
 |hp=1870
 |dp=50
 |pp=20
 |c_attack=Fire Tornado
 |c_attack_jp=ホーリーフレイム
 |c_attack_jp_roman=Holy Flame
 |c_pow=800
 |t_attack=Apocalypse
 |t_attack_jp=アポカリプス
 |t_attack_jp_roman=
 |t_pow=610
 |x_attack=Hermit Fog
 |x_attack_jp=ハーミットフォッグ
 |x_attack_jp_roman=
 |x_pow=370
 |x_effect={{button|x}} to 0
 |support={{button|x}} Counterattack. Attack second.
}}
{{-}}

==072: AeroVeedramon==
{{Card Infobox DDCB-DM
 |name=AeroVeedramon
 |name_jp=エアロ{{ruby|V|ブイ}}ドラモン
 |name_jp_roman=EaroV-dramon
 |number=072
 |level=U
 |specialty=Nature
 |hp=1430
 |dp=40
 |pp=20
 |c_attack=V Wing Blade
 |c_attack_jp=Ｖウイングブレード
 |c_attack_jp_roman=
 |c_pow=750
 |t_attack=Twister Saber
 |t_attack_jp=ツイスターセイバー
 |t_attack_jp_roman=
 |t_pow=550
 |x_attack=Magnum Clash
 |x_attack_jp=マグナムクラッシュ
 |x_attack_jp_roman=
 |x_pow=360
 |x_effect=1st Attack
 |support=If own level is U, own Attack Power is doubled.
}}
{{-}}

==073: Rosemon==
{{Card Infobox DDCB-DM
 |name=Rosemon
 |name_jp=ロゼモン
 |name_jp_roman=
 |number=073
 |level=U
 |specialty=Nature
 |hp=1210
 |dp=40
 |pp=30
 |c_attack=Thorny Whipping
 |c_attack_jp=ソーンウィップ
 |c_attack_jp_roman=Thorn Whip
 |c_pow=720
 |t_attack=Rose Spear
 |t_attack_jp=ローゼスレイピア
 |t_attack_jp_roman=Roses Rapier
 |t_pow=480
 |x_attack=Facination
 |x_attack_jp=ファッシネイション
 |x_attack_jp_roman=Fascination
 |x_pow=320
 |x_effect=Eat-up HP
 |support=If opponent's HP are 1000+, own attack becomes "Eat-up HP."
}}
{{-}}

==074: HerculesKabuterimon==
{{Card Infobox DDCB-DM
 |name=HerculesKabuterimon
 |name_jp=ヘラクルカブテリモン
 |name_jp_roman=HerakleKabuterimon
 |number=074
 |level=U
 |specialty=Nature
 |hp=1700
 |dp=40
 |pp=20
 |c_attack=Giga Scissor Claw
 |c_attack_jp=ギガブラスター
 |c_attack_jp_roman=Giga Blaster
 |c_pow=790
 |t_attack=Hyper Mega Blaster
 |t_attack_jp=ハイメガブラスター
 |t_attack_jp_roman=High Mega Blaster
 |t_pow=490
 |x_attack=Horn Buster II
 |x_attack_jp=ホーンバスター改
 |x_attack_jp_roman=Horn Buster Kai
 |x_pow=250
 |x_effect=1st Attack
 |support=None
}}
{{-}}

==075: MagnaAngemon==
{{Card Infobox DDCB-DM
 |name=MagnaAngemon
 |name_jp=ホーリーエンジェモン
 |name_jp_roman=HolyAngemon
 |number=075
 |level=U
 |specialty=Nature
 |hp=1320
 |dp=40
 |pp=20
 |c_attack=The Gate of Destiny
 |c_attack_jp=ヘブンズゲート
 |c_attack_jp_roman=Heaven's Gate
 |c_pow=770
 |t_attack=Excalibur
 |t_attack_jp=エクスキャリバー
 |t_attack_jp_roman=
 |t_pow=570
 |x_attack=Soul Vanisher
 |x_attack_jp=ソウルバニッシュ
 |x_attack_jp_roman=Soul Banish
 |x_pow=370
 |x_effect=Darkness Foe x3
 |support=If opponent's Specialty is Darkness, boost own Attack Power +500.
}}
{{-}}

==076: Silphymon==
{{Card Infobox DDCB-DM
 |name=Silphymon
 |name_jp=シルフィーモン
 |name_jp_roman=
 |number=076
 |level=U
 |specialty=Nature
 |hp=1540
 |dp=40
 |pp=20
 |c_attack=Top Gun
 |c_attack_jp=トップガン
 |c_attack_jp_roman=
 |c_pow=680
 |t_attack=Dual Sonic Boom
 |t_attack_jp=デュアルソニック
 |t_attack_jp_roman=Dual Sonic
 |t_pow=500
 |x_attack=Air Field
 |x_attack_jp=エアフィールド
 |x_attack_jp_roman=
 |x_pow=400
 |x_effect={{button|t}} to 0
 |support=If opponent's Specialty is not Nature, attack second.
}}
{{-}}

==077: Angewomon==
{{Card Infobox DDCB-DM
 |name=Angewomon
 |name_jp=エンジェウーモン
 |name_jp_roman=
 |number=077
 |level=U
 |specialty=Nature
 |hp=1370
 |dp=40
 |pp=30
 |c_attack=Celestial Arrow
 |c_attack_jp=ホーリーアロー
 |c_attack_jp_roman=Holy Arrow
 |c_pow=720
 |t_attack=Heaven's Charm
 |t_attack_jp=ヘブンズチャーム
 |t_attack_jp_roman=
 |t_pow=520
 |x_attack=Holy Air
 |x_attack_jp=セイントエア
 |x_attack_jp_roman=Saint Air
 |x_pow=330
 |x_effect=Darkness Foe x3
 |support=If opponent's Specialty is Darkness, recover own HP by +500.
}}
{{-}}

==078: Lillymon==
{{Card Infobox DDCB-DM
 |name=Lillymon
 |name_jp=リリモン
 |name_jp_roman=Lilimon
 |number=078
 |level=U
 |specialty=Nature
 |hp=1100
 |dp=30
 |pp=30
 |c_attack=Flower Cannon
 |c_attack_jp=フラウカノン
 |c_attack_jp_roman=Flow' Cannon
 |c_pow=650
 |t_attack=Vicious Vine
 |t_attack_jp=フェアリーバイン
 |t_attack_jp_roman=Fairy Vine
 |t_pow=340
 |x_attack=Temptation
 |x_attack_jp=テンプテーション
 |x_attack_jp_roman=
 |x_pow=200
 |x_effect=Eat-up HP
 |support=Recover own HP by +200.
}}
{{-}}

==079: MegaKabuterimon==
{{Card Infobox DDCB-DM
 |name=MegaKabuterimon
 |name_link=MegaKabuterimon (Red)
 |name_jp=アトラーカブテリモン
 |name_jp_roman=AtlurKabuterimon
 |number=079
 |level=U
 |specialty=Nature
 |hp=1480
 |dp=30
 |pp=20
 |c_attack=Horn Buster
 |c_attack_jp=ホーンバスター
 |c_attack_jp_roman=
 |c_pow=700
 |t_attack=Electro Shocker
 |t_attack_jp=メガブラスター
 |t_attack_jp_roman=Mega Blaster
 |t_pow=400
 |x_attack=Wild Scratcher
 |x_attack_jp=ワイルドスクラッチ
 |x_attack_jp_roman=Wild Scratch
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=None
}}
{{-}}

==080: Piximon==
{{Card Infobox DDCB-DM
 |name=Piximon
 |name_jp=ピッコロモン
 |name_jp_roman=Picklemon
 |number=080
 |level=U
 |specialty=Nature
 |hp=1370
 |dp=40
 |pp=30
 |c_attack=BIT Bomb
 |c_attack_jp=ビットボム
 |c_attack_jp_roman=
 |c_pow=670
 |t_attack=Fairy Tale
 |t_attack_jp=フェアリーテイル
 |t_attack_jp_roman=
 |t_pow=430
 |x_attack=Victory Trick
 |x_attack_jp=ピクトトリック
 |x_attack_jp_roman=Pict Trick
 |x_pow=320
 |x_effect=None
 |support=Opponent's Support Effect is voided. Own Attack Power is halved.
}}
{{-}}

==081: Veedramon==
{{Card Infobox DDCB-DM
 |name=Veedramon
 |name_jp=ブイドラモン
 |name_jp_roman=V-dramon
 |number=081
 |level=C
 |specialty=Nature
 |hp=880
 |dp=40
 |pp=20
 |c_attack=V-Nova Blast
 |c_attack_jp=Ｖブレスアロー
 |c_attack_jp_roman=V Breath Arrow
 |c_pow=500
 |t_attack=Hammer Punch
 |t_attack_jp=ハンマーパンチ
 |t_attack_jp_roman=
 |t_pow=360
 |x_attack=Cutting Shoot
 |x_attack_jp=カッターシュート
 |x_attack_jp_roman=Cutter Shoot
 |x_pow=200
 |x_effect=1st Attack
 |support=If own level is U, own Attack Power is doubled.
}}
{{-}}

==082: Angemon==
{{Card Infobox DDCB-DM
 |name=Angemon
 |name_jp=エンジェモン
 |name_jp_roman=
 |number=082
 |level=C
 |specialty=Nature
 |hp=940
 |dp=40
 |pp=20
 |c_attack=Hand of Fate
 |c_attack_jp=ヘブンズナックル
 |c_attack_jp_roman=Heaven's Knuckle
 |c_pow=400
 |t_attack=Omni Typhoon
 |t_attack_jp=ゴッドタイフーン
 |t_attack_jp_roman=God Typhoon
 |t_pow=200
 |x_attack=Holy Rod
 |x_attack_jp=ホーリーロッド
 |x_attack_jp_roman=
 |x_pow=260
 |x_effect=Darkness Foe x3
 |support=If opponent's Specialty is Darkness, own Attack Power is tripled.
}}
{{-}}

==083: R-Gatomon==
{{Card Infobox DDCB-DM
 |name=R-Gatomon
 |name_jp=テイルモンR
 |name_jp_roman=Tailmon R
 |number=083
 |level=C
 |specialty=Nature
 |hp=750
 |dp=30
 |pp=20
 |c_attack=Lightning Paw
 |c_attack_jp=ネコパンチ
 |c_attack_jp_roman=Neko Punch
 |c_pow=410
 |t_attack=Lightning Kick
 |t_attack_jp=ネコキック
 |t_attack_jp_roman=Neko Kick
 |t_pow=300
 |x_attack=Cat's Eyes
 |x_attack_jp=キャッツ・アイ
 |x_attack_jp_roman=Cat's Eye
 |x_pow=210
 |x_effect={{button|x}} to 0
 |support=If own HP are less than 500, boost own Attack Power +300.
}}
{{-}}

==084: Togemon==
{{Card Infobox DDCB-DM
 |name=Togemon
 |name_jp=トゲモン
 |name_jp_roman=
 |number=084
 |level=C
 |specialty=Nature
 |hp=800
 |dp=30
 |pp=30
 |c_attack=Needle Spray
 |c_attack_jp=チクチクバンバン
 |c_attack_jp_roman=Chikuchiku Bang Bang
 |c_pow=380
 |t_attack=Coconut Punch
 |t_attack_jp=ココナッツパンチ
 |t_attack_jp_roman=Coconuts Punch
 |t_pow=250
 |x_attack=Fast Jab
 |x_attack_jp=マッハジャブ
 |x_attack_jp_roman=Mach Jab
 |x_pow=170
 |x_effect={{button|t}} to 0
 |support=Boost own Attack Power +100.
}}
{{-}}

==085: Leomon==
{{Card Infobox DDCB-DM
 |name=Leomon
 |name_jp=レオモン
 |name_jp_roman=
 |number=085
 |level=C
 |specialty=Nature
 |hp=890
 |dp=40
 |pp=20
 |c_attack=Beast King's Fist
 |c_attack_jp=獣王拳
 |c_attack_jp_roman=Jūouken
 |c_pow=430
 |t_attack=Lion Sword
 |t_attack_jp=獅子王丸
 |t_attack_jp_roman=Shishiou-maru
 |t_pow=280
 |x_attack=Smashing Kick
 |x_attack_jp=破砕蹴り
 |x_attack_jp_roman=Hasaigeri
 |x_pow=200
 |x_effect=None
 |support=If own level is lower, boost own Attack Power +500.
}}
{{-}}

==086: Kabuterimon==
{{Card Infobox DDCB-DM
 |name=Kabuterimon
 |name_jp=カブテリモン
 |name_jp_roman=
 |number=086
 |level=C
 |specialty=Nature
 |hp=950
 |dp=40
 |pp=20
 |c_attack=Electro Shocker
 |c_attack_jp=メガブラスター
 |c_attack_jp_roman=Mega Blaster
 |c_pow=550
 |t_attack=Big Horn
 |t_attack_jp=ビートホーン
 |t_attack_jp_roman=Beet Horn
 |t_pow=360
 |x_attack=Quick Thrust
 |x_attack_jp=ブリンクスラスト
 |x_attack_jp_roman=Blink Thrust
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=None
}}
{{-}}

==087: Airdramon==
{{Card Infobox DDCB-DM
 |name=Airdramon
 |name_jp=エアドラモン
 |name_jp_roman=
 |number=087
 |level=C
 |specialty=Nature
 |hp=950
 |dp=40
 |pp=20
 |c_attack=Spinning Needle
 |c_attack_jp=スピニングニードル
 |c_attack_jp_roman=
 |c_pow=430
 |t_attack=Wing Cutter
 |t_attack_jp=ウイングカッター
 |t_attack_jp_roman=
 |t_pow=200
 |x_attack=Tail Whip
 |x_attack_jp=テイルウィップ
 |x_attack_jp_roman=
 |x_pow=50
 |x_effect={{button|c}} to 0
 |support=Recover own HP by +100. Boost own Attack Power by +100.
}}
{{-}}

==088: Unimon==
{{Card Infobox DDCB-DM
 |name=Unimon
 |name_jp=ユニモン
 |name_jp_roman=
 |number=088
 |level=C
 |specialty=Nature
 |hp=950
 |dp=40
 |pp=20
 |c_attack=Aerial Attack
 |c_attack_jp=ホーリーショット
 |c_attack_jp_roman=Holy Shot
 |c_pow=390
 |t_attack=Javelin Thrust
 |t_attack_jp=コーンスラスト
 |t_attack_jp_roman='corn Thrust
 |t_pow=210
 |x_attack=Spread Nails
 |x_attack_jp=スプレッドネイ
 |x_attack_jp_roman=Spread Neigh
 |x_pow=150
 |x_effect={{button|c}} to 0
 |support=If opponent's Specialty is Darkness, lower opponent's Attack Power to 0.
}}
{{-}}

==089: Ninjamon==
{{Card Infobox DDCB-DM
 |name=Ninjamon
 |name_jp=イガモン
 |name_jp_roman=Igamon
 |number=089
 |level=C
 |specialty=Nature
 |hp=650
 |dp=30
 |pp=30
 |c_attack=Ninja Knife Throw
 |c_attack_jp=イガ流手裏剣投げ
 |c_attack_jp_roman=Iga-ryuu Shuriken Nage
 |c_pow=440
 |t_attack=Dancing Leaves
 |t_attack_jp=木の葉乱舞
 |t_attack_jp_roman=Konoha Ranbu
 |t_pow=350
 |x_attack=Ninja Jujitsu
 |x_attack_jp=イガ流居合術
 |x_attack_jp_roman=Iga-ryuu Iaijutsu
 |x_pow=250
 |x_effect=1st Attack
 |support=Attack first.
}}
{{-}}

==090: Kuwagamon==
{{Card Infobox DDCB-DM
 |name=Kuwagamon
 |name_jp=クワガーモン
 |name_jp_roman=
 |number=090
 |level=C
 |specialty=Nature
 |hp=900
 |dp=40
 |pp=20
 |c_attack=Scissor Claw
 |c_attack_jp=シザーアームズ
 |c_attack_jp_roman=Scissor Arms
 |c_pow=530
 |t_attack=Power Guillotine
 |t_attack_jp=パワーギロチン
 |t_attack_jp_roman=
 |t_pow=400
 |x_attack=Trapping Scissors
 |x_attack_jp=トラップシザーズ
 |x_attack_jp_roman=Trap Scissors
 |x_pow=0
 |x_effect={{button|t}} Counter
 |support=None
}}
{{-}}

==091: Drimogemon==
{{Card Infobox DDCB-DM
 |name=Drimogemon
 |name_jp=ドリモゲモン
 |name_jp_roman=
 |number=091
 |level=C
 |specialty=Nature
 |hp=850
 |dp=30
 |pp=20
 |c_attack=Iron Drill Spin
 |c_attack_jp=ドリルスピン
 |c_attack_jp_roman=Drill Spin
 |c_pow=450
 |t_attack=Bone Crusher
 |t_attack_jp=クラッシャーボーン
 |t_attack_jp_roman=Crusher Bone
 |t_pow=310
 |x_attack=Screw Claw
 |x_attack_jp=スクリュークロー
 |x_attack_jp_roman=
 |x_pow=280
 |x_effect=None
 |support=Boost own Attack Power +200.
}}
{{-}}

==092: Vegiemon==
{{Card Infobox DDCB-DM
 |name=Vegiemon
 |name_jp=ベジーモン
 |name_jp_roman=Vegimon
 |number=092
 |level=C
 |specialty=Nature
 |hp=810
 |dp=30
 |pp=20
 |c_attack=Compost Bomber
 |c_attack_jp=ウンチ投げ
 |c_attack_jp_roman=Unchi Nage
 |c_pow=390
 |t_attack=Sharp Leaf
 |t_attack_jp=シャープリーフ
 |t_attack_jp_roman=
 |t_pow=270
 |x_attack=Sweet Whisper
 |x_attack_jp=甘い吐息
 |x_attack_jp_roman=Amai Toiki
 |x_pow=100
 |x_effect=Jamming
 |support=Changes opponent's Specialty to Nature.
}}
{{-}}

==093: Kokatorimon==
{{Card Infobox DDCB-DM
 |name=Kokatorimon
 |name_jp=コカトリモン
 |name_jp_roman=Cockatrimon
 |number=093
 |level=C
 |specialty=Nature
 |hp=910
 |dp=30
 |pp=20
 |c_attack=Frozen Fire Shot
 |c_attack_jp=ペトラファイアー
 |c_attack_jp_roman=Petra Fire
 |c_pow=350
 |t_attack=Sliding Beak
 |t_attack_jp=ビークスライド
 |t_attack_jp_roman=Beak Slide
 |t_pow=260
 |x_attack=Gangster
 |x_attack_jp=アゲインスター
 |x_attack_jp_roman=Again Star
 |x_pow=150
 |x_effect={{button|c}} to 0
 |support=Lower opponent's Attack Power to 0. Opponent's HP are doubled.
}}
{{-}}

==094: Yanmamon==
{{Card Infobox DDCB-DM
 |name=Yanmamon
 |name_jp=ヤンマモン
 |name_jp_roman=
 |number=094
 |level=C
 |specialty=Nature
 |hp=740
 |dp=20
 |pp=20
 |c_attack=Thunder Ray
 |c_attack_jp=サンダーレイ
 |c_attack_jp_roman=
 |c_pow=400
 |t_attack=Bug Swarm
 |t_attack_jp=インセクスォーム
 |t_attack_jp_roman=Insect Swarm
 |t_pow=250
 |x_attack=Somersault Attack
 |x_attack_jp=サマーソルトキル
 |x_attack_jp_roman=Somersault Kill
 |x_pow=170
 |x_effect=1st Attack
 |support=None
}}
{{-}}

==095: J-Mojyamon==
{{Card Infobox DDCB-DM
 |name=J-Mojyamon
 |name_jp=ジャングルモジャモン
 |name_jp_roman=JungleMojyamon
 |number=095
 |level=C
 |specialty=Nature
 |hp=750
 |dp=30
 |pp=30
 |c_attack=Jungle Punch
 |c_attack_jp=ジャングルパンチ
 |c_attack_jp_roman=
 |c_pow=280
 |t_attack=Jungle Bone
 |t_attack_jp=ジャングルボーン
 |t_attack_jp_roman=
 |t_pow=250
 |x_attack=Jungle Head Butt
 |x_attack_jp=ジャングルヘッド
 |x_attack_jp_roman=Jungle Head
 |x_pow=180
 |x_effect=None
 |support=If own Level is R, boost own Attack Power +300.
}}
{{-}}

==096: MoriShellmon==
{{Card Infobox DDCB-DM
 |name=MoriShellmon
 |name_jp=モリシェルモン
 |name_jp_roman=
 |number=096
 |level=C
 |specialty=Nature
 |hp=910
 |dp=40
 |pp=30
 |c_attack=Shell Pile
 |c_attack_jp=パイルシェル
 |c_attack_jp_roman=Pile Shell
 |c_pow=390
 |t_attack=Mind Fog
 |t_attack_jp=マインドフォッグ
 |t_attack_jp_roman=
 |t_pow=240
 |x_attack=Invisible Tackle
 |x_attack_jp=カムフラタックル
 |x_attack_jp_roman=Camofla Tackle
 |x_pow=190
 |x_effect={{button|c}} to 0
 |support=If opponent's Specialty is Darkness, lower opponent's Attack Power -200.
}}
{{-}}

==097: Tentomon==
{{Card Infobox DDCB-DM
 |name=Tentomon
 |name_jp=テントモン
 |name_jp_roman=
 |number=097
 |level=R
 |specialty=Nature
 |hp=670
 |dp=0
 |pp=30
 |c_attack=Blue Blaster
 |c_attack_jp=プチサンダー
 |c_attack_jp_roman=Petit Thunder
 |c_pow=380
 |t_attack=Double Punch
 |t_attack_jp=トワイスアーム
 |t_attack_jp_roman=Twice Arm
 |t_pow=220
 |x_attack=Rolling Guard
 |x_attack_jp=ローリングガード
 |x_attack_jp_roman=
 |x_pow=160
 |x_effect={{button|c}} to 0
 |support=None
}}
{{-}}

==098: Palmon==
{{Card Infobox DDCB-DM
 |name=Palmon
 |name_jp=パルモン
 |name_jp_roman=
 |number=098
 |level=R
 |specialty=Nature
 |hp=500
 |dp=0
 |pp=30
 |c_attack=Poison Ivy
 |c_attack_jp=ポイズンアイビー
 |c_attack_jp_roman=
 |c_pow=370
 |t_attack=Plant Shock
 |t_attack_jp=プラントショック
 |t_attack_jp_roman=
 |t_pow=240
 |x_attack=Root Breaker
 |x_attack_jp=ルートストレッチ
 |x_attack_jp_roman=Root Stretch
 |x_pow=160
 |x_effect=Eat-up HP
 |support=None
}}
{{-}}

==099: Salamon==
{{Card Infobox DDCB-DM
 |name=Salamon
 |name_jp=プロットモン
 |name_jp_roman=Plotmon
 |number=099
 |level=R
 |specialty=Nature
 |hp=600
 |dp=0
 |pp=30
 |c_attack=Puppy Howling
 |c_attack_jp=パピーハウリング
 |c_attack_jp_roman=
 |c_pow=300
 |t_attack=Petit Punch
 |t_attack_jp=プチパンチ
 |t_attack_jp_roman=
 |t_pow=230
 |x_attack=Sledge Crash
 |x_attack_jp=スレッジダッシュ
 |x_attack_jp_roman=Sledge Dash
 |x_pow=0
 |x_effect={{button|t}} Counter
 |support=Changes own Specialty to Nature. Draw 1 Card.
}}
{{-}}

==100: Elecmon==
{{Card Infobox DDCB-DM
 |name=Elecmon
 |name_jp=エレキモン
 |name_jp_roman=
 |number=100
 |level=R
 |specialty=Nature
 |hp=650
 |dp=0
 |pp=20
 |c_attack=Super Thunder Strike
 |c_attack_jp=スパークリング{{ruby|Ｔ|サンダー}}
 |c_attack_jp_roman=Sparkling Thunder
 |c_pow=310
 |t_attack=Nine Tails
 |t_attack_jp=ナインテイルス
 |t_attack_jp_roman=
 |t_pow=240
 |x_attack=Lightning Knife
 |x_attack_jp=サンダーナイフ
 |x_attack_jp_roman=Thunder Knife
 |x_pow=130
 |x_effect=Ice Foe x3
 |support=If opponent's Specialty is Ice, boost own Attack Power +300.
}}
{{-}}

==101: Gotsumon==
{{Card Infobox DDCB-DM
 |name=Gotsumon
 |name_jp=ゴツモン
 |name_jp_roman=
 |number=101
 |level=R
 |specialty=Nature
 |hp=700
 |dp=0
 |pp=20
 |c_attack=Rock Fist
 |c_attack_jp=アングリーロック
 |c_attack_jp_roman=Angry Rock
 |c_pow=290
 |t_attack=Hardest Punch
 |t_attack_jp=ハーデストパンチ
 |t_attack_jp_roman=
 |t_pow=180
 |x_attack=Earth Shaker
 |x_attack_jp=アースシェイカー
 |x_attack_jp_roman=
 |x_pow=130
 |x_effect={{button|x}} to 0
 |support=If own HP are more than opponent's HP, own Attack Power is doubled.
}}
{{-}}

==102: Kunemon==
{{Card Infobox DDCB-DM
 |name=Kunemon
 |name_jp=クネモン
 |name_jp_roman=
 |number=102
 |level=R
 |specialty=Nature
 |hp=680
 |dp=0
 |pp=20
 |c_attack=Electric Thread
 |c_attack_jp={{ruby|ＥＬＣ|エレクトリック}}スレッド
 |c_attack_jp_roman=
 |c_pow=350
 |t_attack=Poison Ride
 |t_attack_jp=ポイズンライド
 |t_attack_jp_roman=
 |t_pow=220
 |x_attack=Speeding Thread
 |x_attack_jp=パルジィスレッド
 |x_attack_jp_roman=Palsy Thread
 |x_pow=190
 |x_effect=Jamming
 |support=Lower both Attack Powers -200.
}}
{{-}}

==103: Apokarimon==
{{Card Infobox DDCB-DM
 |name=Apokarimon
 |name_jp=アポカリモン
 |name_jp_roman=Apoclymon
 |number=103
 |level=U
 |specialty=Darkness
 |hp=2750
 |dp=70
 |pp=0
 |c_attack=Darkness Zone
 |c_attack_jp=ダークネスゾーン
 |c_attack_jp_roman=
 |c_pow=990
 |t_attack=Dark Evolution
 |t_attack_jp=デスエボリューション
 |t_attack_jp_roman=Death Evolution
 |t_pow=680
 |x_attack=Grand Big Bang
 |x_attack_jp=グランデスビッグバン
 |x_attack_jp_roman=Gran Death Big Bang
 |x_pow=0
 |x_effect=Crash
 |support=Own HP are halved. Change own Specialty to Darkness.
}}
{{-}}

==104: GranKuwagamon==
{{Card Infobox DDCB-DM
 |name=GranKuwagamon
 |name_jp=グランクワガーモン
 |name_jp_roman=
 |number=104
 |level=U
 |specialty=Darkness
 |hp=1760
 |dp=50
 |pp=10
 |c_attack=X-Scissor Claw
 |c_attack_jp=ディメンジョンシザー
 |c_attack_jp_roman=Dimension Scissor
 |c_pow=800
 |t_attack=Grand Darkness
 |t_attack_jp=グランデススクリュー
 |t_attack_jp_roman=Grand Death Screw
 |t_pow=700
 |x_attack=Z Black Hole
 |x_attack_jp=ゾーンブラックホール
 |x_attack_jp_roman=Zone Black Hole
 |x_pow=600
 |x_effect=None
 |support=Discard 7 Cards from own Online Deck. Opponent's HP are halved.
}}
{{-}}

==105: Diaboromon==
{{Card Infobox DDCB-DM
 |name=Diaboromon
 |name_jp=ディアボロモン
 |name_jp_roman=Diablomon
 |number=105
 |level=U
 |specialty=Darkness
 |hp=2580
 |dp=70
 |pp=0
 |c_attack=Inferno Missile
 |c_attack_jp=カタストロフィキャノン
 |c_attack_jp_roman=Catastrophe Cannon
 |c_pow=970
 |t_attack=Tentacle Bug
 |t_attack_jp=テンタクルバグ
 |t_attack_jp_roman=
 |t_pow=720
 |x_attack=Lost Paradise
 |x_attack_jp=パラダイスロスト
 |x_attack_jp_roman=Paradise Lost
 |x_pow=0
 |x_effect=Crash
 |support=Own HP become 10. Changes opponent's Specialty to Darkness.
}}
{{-}}

==106: VenomMyotismon==
{{Card Infobox DDCB-DM
 |name=VenomMyotismon
 |name_jp=ヴェノムヴァンデモン
 |name_jp_roman=VenomVamdemon
 |number=106
 |level=U
 |specialty=Darkness
 |hp=2310
 |dp=60
 |pp=0
 |c_attack=Venom Infusion
 |c_attack_jp=ヴェノムインフューズ
 |c_attack_jp_roman=Venom Infuse
 |c_pow=920
 |t_attack=Tyrant Savage
 |t_attack_jp=タイラントサベージ
 |t_attack_jp_roman=
 |t_pow=530
 |x_attack=Chaos Flame
 |x_attack_jp=カオスフレイム
 |x_attack_jp_roman=
 |x_pow=400
 |x_effect=Nature Foe x3
 |support=None
}}
{{-}}

==107: Piedmon==
{{Card Infobox DDCB-DM
 |name=Piedmon
 |name_jp=ピエモン
 |name_jp_roman=Piemon
 |number=107
 |level=U
 |specialty=Darkness
 |hp=1650
 |dp=50
 |pp=10
 |c_attack=Trump Sword
 |c_attack_jp=トランプソード
 |c_attack_jp_roman=
 |c_pow=800
 |t_attack=Finishing Sniper
 |t_attack_jp=エンディングスナイプ
 |t_attack_jp_roman=Ending Snipe
 |t_pow=500
 |x_attack=Clown's Trick
 |x_attack_jp=クラウントリック
 |x_attack_jp_roman=Clown Trick
 |x_pow=400
 |x_effect=Jamming
 |support=Both players discard all Cards in Hands.
}}
{{-}}

==108: Machinedramon==
{{Card Infobox DDCB-DM
 |name=Machinedramon
 |name_jp=ムゲンドラモン
 |name_jp_roman=Mugendramon
 |number=108
 |level=U
 |specialty=Darkness
 |hp=2400
 |dp=60
 |pp=0
 |c_attack=Giga Cannon
 |c_attack_jp=ムゲンキャノン
 |c_attack_jp_roman=Mugen Cannon
 |c_pow=980
 |t_attack=Booster Claw
 |t_attack_jp=ブースタークロー
 |t_attack_jp_roman=
 |t_pow=520
 |x_attack=Catastrophic Day
 |x_attack_jp=カタストロフデイ
 |x_attack_jp_roman=Catastrophe Day
 |x_pow=0
 |x_effect=Crash
 |support=None
}}
{{-}}

==109: Infermon==
{{Card Infobox DDCB-DM
 |name=Infermon
 |name_jp=インフェルモン
 |name_jp_roman=
 |number=109
 |level=U
 |specialty=Darkness
 |hp=1100
 |dp=20
 |pp=0
 |c_attack=Hades' Grenade
 |c_attack_jp=ヘルズグレネード
 |c_attack_jp_roman=
 |c_pow=610
 |t_attack=Cocoon Crash
 |t_attack_jp=コクーンアタック
 |t_attack_jp_roman=Cocoon Attack
 |t_pow=370
 |x_attack=Virus Shot
 |x_attack_jp=ウイルススケーター
 |x_attack_jp_roman=Virus Skater
 |x_pow=180
 |x_effect=Jamming
 |support=Discard 5 Cards from own Online Deck. Boost own Attack Power +400.
}}
{{-}}

==110: LadyDevimon==
{{Card Infobox DDCB-DM
 |name=LadyDevimon
 |name_jp=レディデビモン
 |name_jp_roman=
 |number=110
 |level=U
 |specialty=Darkness
 |hp=1150
 |dp=40
 |pp=20
 |c_attack=Darkness Wave
 |c_attack_jp=ダークネスウェーブ
 |c_attack_jp_roman=
 |c_pow=620
 |t_attack=Darkness Spear
 |t_attack_jp=ダークネススピア
 |t_attack_jp_roman=
 |t_pow=360
 |x_attack=Poison
 |x_attack_jp=プワゾン
 |x_attack_jp_roman=
 |x_pow=250
 |x_effect=Eat-up HP
 |support=Both players boost Attack Power +200.
}}
{{-}}

==111: Myotismon==
{{Card Infobox DDCB-DM
 |name=Myotismon
 |name_jp=ヴァンデモン
 |name_jp_roman=Vamdemon
 |number=111
 |level=U
 |specialty=Darkness
 |hp=1100
 |dp=50
 |pp=20
 |c_attack=Grisly Wing
 |c_attack_jp=ナイトレイド
 |c_attack_jp_roman=Night Raid
 |c_pow=650
 |t_attack=Cloud Minion
 |t_attack_jp=クラウドミニオン
 |t_attack_jp_roman=
 |t_pow=400
 |x_attack=Bloody Storm
 |x_attack_jp=ブラッディストリーム
 |x_attack_jp_roman=Bloody Stream
 |x_pow=300
 |x_effect=Eat-up HP
 |support=Digimon KO'd in battle revives with 500 HP. Battle is still lost.
}}
{{-}}

==112: Megadramon==
{{Card Infobox DDCB-DM
 |name=Megadramon
 |name_jp=メガドラモン
 |name_jp_roman=
 |number=112
 |level=U
 |specialty=Darkness
 |hp=1810
 |dp=50
 |pp=0
 |c_attack=Darkside Attack
 |c_attack_jp=ジェノサイドアタック
 |c_attack_jp_roman=Genocide Attack
 |c_pow=920
 |t_attack=Big Mega Fire
 |t_attack_jp=メガデスサイズ
 |t_attack_jp_roman=Mega Death Scythe
 |t_pow=290
 |x_attack=Ultimate Attack
 |x_attack_jp=アルティメット{{ruby|Ｓ|スライザー}}
 |x_attack_jp_roman=Ultimate Slicer
 |x_pow=300
 |x_effect=1st Attack
 |support=Both players' HP are halved.
}}
{{-}}

==113: SkullGreymon==
{{Card Infobox DDCB-DM
 |name=SkullGreymon
 |name_jp=スカルグレイモン
 |name_jp_roman=
 |number=113
 |level=U
 |specialty=Darkness
 |hp=1700
 |dp=50
 |pp=0
 |c_attack=Dark Shot II
 |c_attack_jp=グラウンドゼロ改
 |c_attack_jp_roman=Ground Zero Kai
 |c_pow=960
 |t_attack=Dark Shot
 |t_attack_jp=グラウンドゼロ
 |t_attack_jp_roman=Ground Zero
 |t_pow=350
 |x_attack=Buffalo Breathe
 |x_attack_jp=カースブレス
 |x_attack_jp_roman=Curse Breath
 |x_pow=450
 |x_effect=Nature Foe x3
 |support=If opponent's Specialty is Nature, opponent discards all Cards.
}}
{{-}}

==114: Phantomon==
{{Card Infobox DDCB-DM
 |name=Phantomon
 |name_jp=ファントモン
 |name_jp_roman=Fantomon
 |number=114
 |level=U
 |specialty=Darkness
 |hp=1100
 |dp=30
 |pp=0
 |c_attack=Shadow Scythe
 |c_attack_jp=ソウルチョッパー
 |c_attack_jp_roman=Soul Chopper
 |c_pow=600
 |t_attack=Diabolic Star
 |t_attack_jp=ディアボリックスター
 |t_attack_jp_roman=
 |t_pow=400
 |x_attack=Dark Sentence
 |x_attack_jp=死の宣告
 |x_attack_jp_roman=Shi no Senkoku
 |x_pow=300
 |x_effect=Eat-up HP
 |support=Discard 7 Cards from own Online Deck, own Attack is "Eat-up HP."
}}
{{-}}

==115: WaruMonzaemon==
{{Card Infobox DDCB-DM
 |name=WaruMonzaemon
 |name_jp=ワルもんざえモン
 |name_jp_roman=
 |number=115
 |level=U
 |specialty=Darkness
 |hp=1590
 |dp=40
 |pp=0
 |c_attack=Heart Break Attack
 |c_attack_jp=ハートブレイク{{ruby|Ａ|アタック}}
 |c_attack_jp_roman=
 |c_pow=700
 |t_attack=Bear Claw
 |t_attack_jp=ベアークロー
 |t_attack_jp_roman=
 |t_pow=440
 |x_attack=Nasty Step
 |x_attack_jp=ナスティステップ
 |x_attack_jp_roman=
 |x_pow=200
 |x_effect=Jamming
 |support=Own HP become 10. Own Attack Power is doubled.
}}
{{-}}

==116: Andromon==
{{Card Infobox DDCB-DM
 |name=Andromon
 |name_jp=アンドロモン
 |name_jp_roman=
 |number=116
 |level=U
 |specialty=Darkness
 |hp=1700
 |dp=40
 |pp=10
 |c_attack=Lightning Blade
 |c_attack_jp=スパイラルソード
 |c_attack_jp_roman=Spiral Sword
 |c_pow=690
 |t_attack=Gatling Missiles
 |t_attack_jp=ガトリングミサイル
 |t_attack_jp_roman=Gatling Missile
 |t_pow=590
 |x_attack=Weak Slap
 |x_attack_jp=ウィークスラップ
 |x_attack_jp_roman=
 |x_pow=150
 |x_effect=None
 |support=Own HP are halved. Boost own Attack Power +400.
}}
{{-}}

==117: Stingmon==
{{Card Infobox DDCB-DM
 |name=Stingmon
 |name_jp=スティングモン
 |name_jp_roman=
 |number=117
 |level=C
 |specialty=Darkness
 |hp=880
 |dp=40
 |pp=10
 |c_attack=Spiking Strike
 |c_attack_jp={{ruby|ＳＰＫ|スパイキング}}フィニッシュ
 |c_attack_jp_roman=Spiking Finish
 |c_pow=530
 |t_attack=Moon Shooter
 |t_attack_jp=ムーンシューター
 |t_attack_jp_roman=
 |t_pow=370
 |x_attack=Hot Squeeze
 |x_attack_jp=ヘルスクイーズ
 |x_attack_jp_roman=Hell Squeeze
 |x_pow=270
 |x_effect=Eat-up HP
 |support=Discard 1 DP Card from own DP Slot. Boost own Attack Power +200.
}}
{{-}}

==118: Wizardmon==
{{Card Infobox DDCB-DM
 |name=Wizardmon
 |name_jp=ウィザーモン
 |name_jp_roman=Wizarmon
 |number=118
 |level=C
 |specialty=Darkness
 |hp=850
 |dp=40
 |pp=10
 |c_attack=Thunder Ball
 |c_attack_jp=サンダークラウド
 |c_attack_jp_roman=Thunder Cloud
 |c_pow=540
 |t_attack=Magic Game
 |t_attack_jp=マジックゲーム
 |t_attack_jp_roman=
 |t_pow=370
 |x_attack=Vision of Terror
 |x_attack_jp=テラーイリュージョン
 |x_attack_jp_roman=Terror Illusion
 |x_pow=220
 |x_effect=Jamming
 |support=Discard all Cards in own Hand, then draw 2 Cards.
}}
{{-}}

==119: Devidramon==
{{Card Infobox DDCB-DM
 |name=Devidramon
 |name_jp=デビドラモン
 |name_jp_roman=
 |number=119
 |level=C
 |specialty=Darkness
 |hp=1100
 |dp=50
 |pp=10
 |c_attack=Crimson Claw
 |c_attack_jp=クリムゾンネイル
 |c_attack_jp_roman=Crimson Nail
 |c_pow=520
 |t_attack=Red Eye
 |t_attack_jp=レッド・アイ
 |t_attack_jp_roman=
 |t_pow=440
 |x_attack=Dark Gale
 |x_attack_jp=デモニックゲイル
 |x_attack_jp_roman=Demonic Gale
 |x_pow=370
 |x_effect=None
 |support=Own Attack becomes {{button|t}}.
}}
{{-}}

==120: Devimon==
{{Card Infobox DDCB-DM
 |name=Devimon
 |name_jp=デビモン
 |name_jp_roman=
 |number=120
 |level=C
 |specialty=Darkness
 |hp=960
 |dp=40
 |pp=10
 |c_attack=Evil Wing
 |c_attack_jp=デスクロウ
 |c_attack_jp_roman=Death Claw
 |c_pow=490
 |t_attack=Laser Wing
 |t_attack_jp=レザーウィング
 |t_attack_jp_roman=Leather Wing
 |t_pow=350
 |x_attack=Dungeon Curse
 |x_attack_jp=ヘルコントラクト
 |x_attack_jp_roman=Hell Contract
 |x_pow=250
 |x_effect=Nature Foe x3
 |support=If opponent's Specialty is Nature, own Attack Power is tripled.
}}
{{-}}

==121: Tuskmon==
{{Card Infobox DDCB-DM
 |name=Tuskmon
 |name_jp=タスクモン
 |name_jp_roman=
 |number=121
 |level=C
 |specialty=Darkness
 |hp=1150
 |dp=40
 |pp=10
 |c_attack=Slamming Tusk
 |c_attack_jp=パンツァーナックル
 |c_attack_jp_roman=Panzer Knuckle
 |c_pow=410
 |t_attack=Horn Driver
 |t_attack_jp=ホーンドライバー
 |t_attack_jp_roman=
 |t_pow=360
 |x_attack=Bayonet Lancer
 |x_attack_jp=ベイオネットランサー
 |x_attack_jp_roman=
 |x_pow=300
 |x_effect=None
 |support=Own Attack becomes {{button|x}}.
}}
{{-}}

==122: Ogremon==
{{Card Infobox DDCB-DM
 |name=Ogremon
 |name_jp=オーガモン
 |name_jp_roman=Orgemon
 |number=122
 |level=C
 |specialty=Darkness
 |hp=1050
 |dp=40
 |pp=10
 |c_attack=Pummel Whack
 |c_attack_jp=覇王拳
 |c_attack_jp_roman=Haouken
 |c_pow=530
 |t_attack=Bone Mace
 |t_attack_jp=骨こん棒
 |t_attack_jp_roman=Hone Konbou
 |t_pow=320
 |x_attack=Faint Punch
 |x_attack_jp=フェイントパンチ
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect={{button|t}} Counter
 |support=Discard Cards in own DP Slot and multiply Attack Power by number of discards.
}}
{{-}}

==123: Bakemon==
{{Card Infobox DDCB-DM
 |name=Bakemon
 |name_jp=バケモン
 |name_jp_roman=
 |number=123
 |level=C
 |specialty=Darkness
 |hp=860
 |dp=30
 |pp=10
 |c_attack=Dark Claw
 |c_attack_jp=ヘルズハンド
 |c_attack_jp_roman=Hell's Hand
 |c_pow=450
 |t_attack=Ghost Chop
 |t_attack_jp=ゴーストチョップ
 |t_attack_jp_roman=
 |t_pow=270
 |x_attack=Dark Charm
 |x_attack_jp=デスチャーム
 |x_attack_jp_roman=Death Charm
 |x_pow=170
 |x_effect=Eat-up HP
 |support=Change own Specialty to Darkness.
}}
{{-}}

==124: Guardromon==
{{Card Infobox DDCB-DM
 |name=Guardromon
 |name_jp=ガードロモン
 |name_jp_roman=
 |number=124
 |level=C
 |specialty=Darkness
 |hp=750
 |dp=20
 |pp=10
 |c_attack=Protect Grenade
 |c_attack_jp={{ruby|Ｄ|ディストラクション}}グレネード
 |c_attack_jp_roman=Destruction Grenade
 |c_pow=430
 |t_attack=Warning Laser
 |t_attack_jp=ワーニングレーザー
 |t_attack_jp_roman=
 |t_pow=200
 |x_attack=Red Alert
 |x_attack_jp=レッドアラート
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect=Crash
 |support=Own HP are halved. Boost own Attack Power +300.
}}
{{-}}

==125: Tekkamon==
{{Card Infobox DDCB-DM
 |name=Tekkamon
 |name_jp=テッカモン
 |name_jp_roman=
 |number=125
 |level=C
 |specialty=Darkness
 |hp=1100
 |dp=30
 |pp=10
 |c_attack=Electronic Blast Sword
 |c_attack_jp=斬電剣
 |c_attack_jp_roman=Zandenken
 |c_pow=350
 |t_attack=Skull Stand
 |t_attack_jp=スカルスタンド
|t_attack_jp_roman=
 |t_pow=200
 |x_attack=Frag Bomb
 |x_attack_jp=フラグメントボム
 |x_attack_jp_roman=Fragment Bomb
 |x_pow=0
 |x_effect=Crash
 |support=Both players boost Attack Power +300.
}}
{{-}}

==126: Gururumon==
{{Card Infobox DDCB-DM
 |name=Gururumon
 |name_jp=グルルモン
 |name_jp_roman=
 |number=126
 |level=C
 |specialty=Darkness
 |hp=1040
 |dp=40
 |pp=10
 |c_attack=Chaos Blaster
 |c_attack_jp=カオスファイアー
 |c_attack_jp_roman=Chaos Fire
 |c_pow=470
 |t_attack=Karate Kilo Byte
 |t_attack_jp=キラーバイト
 |t_attack_jp_roman=Killer Bite
 |t_pow=340
 |x_attack=Dark Moonsault
 |x_attack_jp=デスムーンサルト
 |x_attack_jp_roman=Death Moonsault
 |x_pow=100
 |x_effect={{button|c}} to 0
 |support=Both players use {{button|t}}.
}}
{{-}}

==127: Soulmon==
{{Card Infobox DDCB-DM
 |name=Soulmon
 |name_jp=ソウルモン
 |name_jp_roman=
 |number=127
 |level=C
 |specialty=Darkness
 |hp=500
 |dp=30
 |pp=0
 |c_attack=Necro Magic
 |c_attack_jp=ネクロマジック
 |c_attack_jp_roman=
 |c_pow=330
 |t_attack=Finishing Trance
 |t_attack_jp=エンドトランス
|t_attack_jp_roman=End Trance
 |t_pow=310
 |x_attack=Energy Drain
 |x_attack_jp=エナジードレイン
 |x_attack_jp_roman=
 |x_pow=290
 |x_effect=Eat-up HP
 |support=Discard 1 Card in DP Slot. change opponent's Specialty to Darkness.
}}
{{-}}

==128: Fugamon==
{{Card Infobox DDCB-DM
 |name=Fugamon
 |name_jp=フーガモン
 |name_jp_roman=
 |number=128
 |level=C
 |specialty=Darkness
 |hp=940
 |dp=30
 |pp=10
 |c_attack=Evil Hurricane
 |c_attack_jp=イビルハリケーン
 |c_attack_jp_roman=
 |c_pow=460
 |t_attack=Heavy Swing
 |t_attack_jp=ヘビースイング
 |t_attack_jp_roman=
 |t_pow=430
 |x_attack=Damp Cloud
 |x_attack_jp=ダンプクラウド
 |x_attack_jp_roman=
 |x_pow=400
 |x_effect=None
 |support=Own Attack becomes {{button|c}}.
}}
{{-}}

==129: Saberdramon==
{{Card Infobox DDCB-DM
 |name=Saberdramon
 |name_jp=セーバードラモン
 |name_jp_roman=
 |number=129
 |level=C
 |specialty=Darkness
 |hp=670
 |dp=30
 |pp=10
 |c_attack=Black Saber
 |c_attack_jp=ブラックセーバー
 |c_attack_jp_roman=
 |c_pow=400
 |t_attack=Nitro Arrow
 |t_attack_jp=ナイトロアー
 |t_attack_jp_roman=Night Roar
 |t_pow=150
 |x_attack=Mach Shadow
 |x_attack_jp=マッハシャドウ
 |x_attack_jp_roman=
 |x_pow=240
 |x_effect=1st Attack
 |support=Both players use {{button|x}}.
}}
{{-}}

==130: Darkrizamon==
{{Card Infobox DDCB-DM
 |name=Darkrizamon
 |name_jp=ダークリザモン
 |name_jp_roman=DarkLizamon
 |number=130
 |level=C
 |specialty=Darkness
 |hp=890
 |dp=30
 |pp=10
 |c_attack=Dark Flare
 |c_attack_jp=ドレッドファイア
 |c_attack_jp_roman=Dread Fire
 |c_pow=330
 |t_attack=Snipping Fang
 |t_attack_jp=スナイプファング
 |t_attack_jp_roman=Snipe Fang
 |t_pow=440
 |x_attack=Dark Pain
 |x_attack_jp=ダークペイン
 |x_attack_jp_roman=
 |x_pow=30
 |x_effect={{button|c}} to 0
 |support=Both players use {{button|c}}.
}}
{{-}}

==131: Zassomon==
{{Card Infobox DDCB-DM
 |name=Zassomon
 |name_jp=ザッソーモン
 |name_jp_roman=Zassoumon
 |number=131
 |level=C
 |specialty=Darkness
 |hp=600
 |dp=20
 |pp=0
 |c_attack=Deadly Ivy
 |c_attack_jp=スクイーズバイン
 |c_attack_jp_roman=Squeeze Vine
 |c_pow=480
 |t_attack=Deadly Weed
 |t_attack_jp=デッドウィード
 |t_attack_jp_roman=Dead Weed
 |t_pow=410
 |x_attack=Head Harvest
 |x_attack_jp=ヘッドハーベスト
 |x_attack_jp_roman=
 |x_pow=350
 |x_effect=None
 |support=Opponent's Attack Power become 300.
}}
{{-}}

==132: DemiDevimon==
{{Card Infobox DDCB-DM
 |name=DemiDevimon
 |name_jp=ピコデビモン
 |name_jp_roman=PicoDevimon
 |number=132
 |level=R
 |specialty=Darkness
 |hp=490
 |dp=0
 |pp=20
 |c_attack=Demi Dart
 |c_attack_jp=ピコダーツ
 |c_attack_jp_roman=Pico Darts
 |c_pow=360
 |t_attack=Evil Wisper
 |t_attack_jp=悪魔のささやき
 |t_attack_jp_roman=Akuma no Sasayaki
 |t_pow=200
 |x_attack=Butt Smasher
 |x_attack_jp=バットフラッター
 |x_attack_jp_roman=Bat Flutter
 |x_pow=190
 |x_effect=Nature Foe x3
 |support=If opponent's Specialty is Nature, own Attack Power is doubled.
}}
{{-}}

==133: BKGatomon==
{{Card Infobox DDCB-DM
 |name=BKGatomon
 |name_jp=ブラックテイルモン
 |name_jp_roman=BlackTailmon
 |number=133
 |level=R
 |specialty=Darkness
 |hp=520
 |dp=0
 |pp=20
 |c_attack=Lightning Paw
 |c_attack_jp=ネコパンチ
 |c_attack_jp_roman=Neko Punch
 |c_pow=360
 |t_attack=Lightning Kick
 |t_attack_jp=ネコキック
 |t_attack_jp_roman=Neko Kick
 |t_pow=300
 |x_attack=Cat's Eyes
 |x_attack_jp=キャッツ・アイ
 |x_attack_jp_roman=Cat's Eye
 |x_pow=240
 |x_effect={{button|x}} to 0
 |support=If opponent's Level is A, opponent's HP are halved.
}}
{{-}}

==134: Kokuwamon==
{{Card Infobox DDCB-DM
 |name=Kokuwamon
 |name_jp=コクワモン
 |name_jp_roman=
 |number=134
 |level=R
 |specialty=Darkness
 |hp=670
 |dp=0
 |pp=20
 |c_attack=Mini Scissor Claws
 |c_attack_jp=シザーアームズミニ
 |c_attack_jp_roman=Scissor Arms Mini
 |c_pow=270
 |t_attack=Stun Shock
 |t_attack_jp=スタンショック
 |t_attack_jp_roman=
 |t_pow=240
 |x_attack=Dis-Assembler
 |x_attack_jp=アッセンブルワーク
 |x_attack_jp_roman=Assemble Work
 |x_pow=200
 |x_effect={{button|t}} to 0
 |support=Reduce own Attack Power by -100. Recover own HP by +200.
}}
{{-}}

==135: Tsukaimon==
{{Card Infobox DDCB-DM
 |name=Tsukaimon
 |name_jp=ツカイモン
 |name_jp_roman=Tukaimon
 |number=135
 |level=R
 |specialty=Darkness
 |hp=630
 |dp=0
 |pp=20
 |c_attack=Evil Spell
 |c_attack_jp=バッドメッセージ
 |c_attack_jp_roman=Bad Message
 |c_pow=240
 |t_attack=Fluffy Attack
 |t_attack_jp=ふわふわアタック
 |t_attack_jp_roman=Fuwafuwa Attack
 |t_pow=200
 |x_attack=Purple Fog
 |x_attack_jp=パープルフォッグ
 |x_attack_jp_roman=
 |x_pow=160
 |x_effect={{button|c}} to 0
 |support=Boost own {{button|x}} Attack Power +200. {{button|c}} & {{button|t}} Attack Power are 0.
}}
{{-}}

==136: Dokunemon==
{{Card Infobox DDCB-DM
 |name=Dokunemon
 |name_jp=ドクネモン
 |name_jp_roman=
 |number=136
 |level=R
 |specialty=Darkness
 |hp=650
 |dp=0
 |pp=20
 |c_attack=Worm Venom
 |c_attack_jp=ワームベノム
 |c_attack_jp_roman=
 |c_pow=280
 |t_attack=Bug Shower
 |t_attack_jp=インセクトホード
 |t_attack_jp_roman=Insect Hold
 |t_pow=220
 |x_attack=Capturing Net
 |x_attack_jp=キャプチャネット
 |x_attack_jp_roman=Capture Net
 |x_pow=190
 |x_effect=Rare Foe x3
 |support=If opponent's Specialty is Rare, opponent's HP become 100.
}}
{{-}}

==137: Aruraumon==
{{Card Infobox DDCB-DM
 |name=Aruraumon
 |name_jp=アルウラモン
 |name_jp_roman=Alraumon
 |number=137
 |level=R
 |specialty=Darkness
 |hp=420
 |dp=0
 |pp=20
 |c_attack=Nemesis Ivy
 |c_attack_jp=ネメシスアイビー
 |c_attack_jp_roman=
 |c_pow=340
 |t_attack=Gloomy Dust
 |t_attack_jp=グルームダスト
 |t_attack_jp_roman=Gloom Dust
 |t_pow=240
 |x_attack=Hungry Hand
 |x_attack_jp=ハングリーハンド
 |x_attack_jp_roman=
 |x_pow=190
 |x_effect=Eat-up HP
 |support=Own Attack becomes "Eat-up HP." Own Attack Power is halved.
}}
{{-}}

==138: Sharmamon==
{{Card Infobox DDCB-DM
 |name=Sharmamon
 |name_jp=シャーマモン
 |name_jp_roman=Shamamon
 |number=138
 |level=R
 |specialty=Darkness
 |hp=570
 |dp=0
 |pp=20
 |c_attack=Sharma Hammer
 |c_attack_jp=シャーマハンマー
 |c_attack_jp_roman=Shama Hammer
 |c_pow=350
 |t_attack=Mad Twister
 |t_attack_jp=マッドツイスト
 |t_attack_jp_roman=
 |t_pow=220
 |x_attack=Dancing Bone
 |x_attack_jp=ダンシングボーン
 |x_attack_jp_roman=
 |x_pow=100
 |x_effect=Jamming
 |support=Opponent's HP are halved. opponent's Attack Power is doubled.
}}
{{-}}

==139: Puppetmon==
{{Card Infobox DDCB-DM
 |name=Puppetmon
 |name_jp=ピノッキモン
 |name_jp_roman=Pinochimon
 |number=139
 |level=U
 |specialty=Rare
 |hp=1540
 |dp=50
 |pp=10
 |c_attack=Puppet Pummel
 |c_attack_jp=ブリットハンマー
 |c_attack_jp_roman=Bullet Hammer
 |c_pow=790
 |t_attack=Clean Sweep
 |t_attack_jp=クリーンアップ
 |t_attack_jp_roman=Clean Up
 |t_pow=570
 |x_attack=Big Liar
 |x_attack_jp=ビッグライアー
 |x_attack_jp_roman=
 |x_pow=380
 |x_effect=Jamming
 |support=Discard 1 of opponent's Cards in DP Slot. Draw 1 Card.
}}
{{-}}

==140: SuperStarmon==
{{Card Infobox DDCB-DM
 |name=SuperStarmon
 |name_jp=スーパースターモン
 |name_jp_roman=
 |number=140
 |level=U
 |specialty=Rare
 |hp=1650
 |dp=40
 |pp=20
 |c_attack=Comet Cluster
 |c_attack_jp=ハレースコール
 |c_attack_jp_roman=Halley Squall
 |c_pow=730
 |t_attack=Galactic Eyes
 |t_attack_jp=ガラクティカアイズ
 |t_attack_jp_roman=Galactica Eyes
 |t_pow=600
 |x_attack=Super Star Seeker
 |x_attack_jp={{ruby|Ｓ|スーパー}}スターシーカー
 |x_attack_jp_roman=
 |x_pow=380
 |x_effect=Rare Foe x3
 |support=If opponent's Specialty is Rare, lower opponent's Attack Power to 0.
}}
{{-}}

==141: MetalEtemon==
{{Card Infobox DDCB-DM
 |name=MetalEtemon
 |name_jp=メタルエテモン
 |name_jp_roman=
 |number=141
 |level=U
 |specialty=Rare
 |hp=1650
 |dp=50
 |pp=10
 |c_attack=Banana Slip
 |c_attack_jp=バナナスリップ
 |c_attack_jp_roman=
 |c_pow=300
 |t_attack=Heavymon Kick
 |t_attack_jp=ヘビーモンキック
 |t_attack_jp_roman=
 |t_pow=750
 |x_attack=Dark Sonic Boom
 |x_attack_jp=ダークリサイタル
 |x_attack_jp_roman=Dark Recital
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support={{button|c}} Counterattack. Attack second.
}}
{{-}}

==142: Shakkoumon==
{{Card Infobox DDCB-DM
 |name=Shakkoumon
 |name_jp=シャッコウモン
 |name_jp_roman=
 |number=142
 |level=U
 |specialty=Rare
 |hp=1760
 |dp=40
 |pp=20
 |c_attack=Clay Bomb
 |c_attack_jp=ニギミタマ
 |c_attack_jp_roman=Nigimitama
 |c_pow=680
 |t_attack=Wild Spirit
 |t_attack_jp=アラミタマ
 |t_attack_jp_roman=Aramitama
 |t_pow=520
 |x_attack=Super Spirit
 |x_attack_jp=サキミタマ
 |x_attack_jp_roman=Sakimitama
 |x_pow=300
 |x_effect=Jamming
 |support=Recover own HP by +100. Boost own {{button|x}} Attack Power by +100.
}}
{{-}}

==143: Jijimon==
{{Card Infobox DDCB-DM
 |name=Jijimon
 |name_jp=ジジモン
 |name_jp_roman=
 |number=143
 |level=U
 |specialty=Rare
 |hp=1260
 |dp=40
 |pp=20
 |c_attack=Dark Noose
 |c_attack_jp=ハング・オン・デス
 |c_attack_jp_roman=Hang on Death
 |c_pow=650
 |t_attack=Gentle Punch
 |t_attack_jp=ジェントルパンチ
 |t_attack_jp_roman=
 |t_pow=560
 |x_attack=Guard Stick
 |x_attack_jp=ガードスティック
 |x_attack_jp_roman=
 |x_pow=250
 |x_effect={{button|t}} to 0
 |support=If opponent's Specialty is Darkness, lower opponent's Attack Power to 0.
}}
{{-}}

==144: Digitamamon==
{{Card Infobox DDCB-DM
 |name=Digitamamon
 |name_jp=デジタマモン
 |name_jp_roman=
 |number=144
 |level=U
 |specialty=Rare
 |hp=1810
 |dp=50
 |pp=10
 |c_attack=Nightmare Syndromer
 |c_attack_jp=ナイトメア{{ruby|ＳＲ|シンドローム}}
 |c_attack_jp_roman=Nightmare Syndrome
 |c_pow=800
 |t_attack=Hyper Flashing
 |t_attack_jp=エニグマ
 |t_attack_jp_roman=Enigma
 |t_pow=540
 |x_attack=Stinky Egg
 |x_attack_jp=スインググエッグ
 |x_attack_jp_roman=Swing Egg
 |x_pow=300
 |x_effect={{button|c}} to 0
 |support=Swap own Specialty with opponent's Specialty.
}}
{{-}}

==145: Vademon==
{{Card Infobox DDCB-DM
 |name=Vademon
 |name_jp=ベーダモン
 |name_jp_roman=
 |number=145
 |level=U
 |specialty=Rare
 |hp=1370
 |dp=40
 |pp=10
 |c_attack=Alien Ray
 |c_attack_jp=アブダクション光線
 |c_attack_jp_roman=Abduction Kousen
 |c_pow=850
 |t_attack=Mutilator
 |t_attack_jp=ムーティレート
 |t_attack_jp_roman=Mutilate
 |t_pow=600
 |x_attack=Evil Kiss
 |x_attack_jp=悪魔の投げキッス
 |x_attack_jp_roman=Akuma no Nage Kiss
 |x_pow=200
 |x_effect=Jamming
 |support=Opponent's Specialty becomes the same as own Specialty.
}}
{{-}}

==146: Giromon==
{{Card Infobox DDCB-DM
 |name=Giromon
 |name_jp=ギロモン
 |name_jp_roman=
 |number=146
 |level=U
 |specialty=Rare
 |hp=1900
 |dp=30
 |pp=10
 |c_attack=Big Bang Boom
 |c_attack_jp=デッドリーボム
 |c_attack_jp_roman=Deadly Bomb
 |c_pow=720
 |t_attack=Guillo-Chain Saw
 |t_attack_jp=ギロチェーンソー
 |t_attack_jp_roman=
 |t_pow=520
 |x_attack=Over Run
 |x_attack_jp=オーバーラン
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect=Crash
 |support=Opponent uses {{button|x}}.
}}
{{-}}

==147: Monzaemon==
{{Card Infobox DDCB-DM
 |name=Monzaemon
 |name_jp=もんざえモン
 |name_jp_roman=
 |number=147
 |level=U
 |specialty=Rare
 |hp=2030
 |dp=50
 |pp=20
 |c_attack=Hearts Attack
 |c_attack_jp=ラブリーアタック
 |c_attack_jp_roman=Lovely Attack
 |c_pow=850
 |t_attack=Bang Bang Punch
 |t_attack_jp=ぶんぶんパンチ
 |t_attack_jp_roman=Bunbun Punch
 |t_pow=500
 |x_attack=Silent Bear Hug
 |x_attack_jp=サイレンスハッグ
 |x_attack_jp_roman=Silence Hug
 |x_pow=430
 |x_effect=Darkness Foe x3
 |support=Recover own HP by +200. Boost own Attack Power by +100.
}}
{{-}}

==148: MetalMamemon==
{{Card Infobox DDCB-DM
 |name=MetalMamemon
 |name_jp=メタルマメモン
 |name_jp_roman=
 |number=148
 |level=U
 |specialty=Rare
 |hp=1920
 |dp=30
 |pp=10
 |c_attack=Energetic Bomb
 |c_attack_jp=エネルギーボム
 |c_attack_jp_roman=Energy Bomb
 |c_pow=770
 |t_attack=Magnetic Beam
 |t_attack_jp=マグネビーム
 |t_attack_jp_roman=Magnet Beam
 |t_pow=570
 |x_attack=Shaft Spike
 |x_attack_jp=シャフトスパイク
 |x_attack_jp_roman=
 |x_pow=280
 |x_effect=1st Attack
 |support=None
}}
{{-}}

==149: Mamemon==
{{Card Infobox DDCB-DM
 |name=Mamemon
 |name_jp=マメモン
 |name_jp_roman=
 |number=149
 |level=U
 |specialty=Rare
 |hp=1700
 |dp=30
 |pp=10
 |c_attack=Smiley Bomb
 |c_attack_jp=スマイリーボム
 |c_attack_jp_roman=
 |c_pow=820
 |t_attack=One-Two Punch
 |t_attack_jp=ワンツーラッシュ
 |t_attack_jp_roman=One-Two Rush
 |t_pow=650
 |x_attack=Diving Attack
 |x_attack_jp=バスターダイブ
 |x_attack_jp_roman=Buster Dive
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=None
}}
{{-}}

==150: Etemon==
{{Card Infobox DDCB-DM
 |name=Etemon
 |name_jp=エテモン
 |name_jp_roman=
 |number=150
 |level=U
 |specialty=Rare
 |hp=1480
 |dp=40
 |pp=20
 |c_attack=Dark Network
 |c_attack_jp=ダークスピリッツ
 |c_attack_jp_roman=Dark Spirits
 |c_pow=700
 |t_attack=Monkey Kick
 |t_attack_jp=モンキック
 |t_attack_jp_roman=Mon-kick
 |t_pow=530
 |x_attack=Concert Crush
 |x_attack_jp=ラブ・セレナーデ
 |x_attack_jp_roman=Love Serenade
 |x_pow=150
 |x_effect=Jamming
 |support=Lower opponent's {{button|x}} Attack Power to 0.
}}
{{-}}

==151: Ankylomon==
{{Card Infobox DDCB-DM
 |name=Ankylomon
 |name_jp=アンキロモン
 |name_jp_roman=
 |number=151
 |level=C
 |specialty=Rare
 |hp=1000
 |dp=40
 |pp=10
 |c_attack=Tail Hammer
 |c_attack_jp=テイルハンマー
 |c_attack_jp_roman=
 |c_pow=420
 |t_attack=Armored Stampede
 |t_attack_jp=アーマースタンピード
 |t_attack_jp_roman=Armor Stampede
 |t_pow=240
 |x_attack=Knock Out Beat
 |x_attack_jp=リズミカルノック
 |x_attack_jp_roman=Rhythmical Knock
 |x_pow=120
 |x_effect={{button|c}} to 0
 |support=If opponent has more than 2 Cards in DP Slot, his Attack Power is 0.
}}
{{-}}

==152: Starmon==
{{Card Infobox DDCB-DM
 |name=Starmon
 |name_jp=スターモン
 |name_jp_roman=
 |number=152
 |level=C
 |specialty=Rare
 |hp=900
 |dp=40
 |pp=10
 |c_attack=Meteor Stream
 |c_attack_jp=メテオスコール
 |c_attack_jp_roman=Meteor Squall
 |c_pow=470
 |t_attack=Hypnotizer
 |t_attack_jp=ヒュプノタイザー
 |t_attack_jp_roman=
 |t_pow=370
 |x_attack=Star Seeker
 |x_attack_jp=スターシーカー
 |x_attack_jp_roman=
 |x_pow=230
 |x_effect=Darkness Foe x3
 |support=If opponent's Specialty is Darkness, opponent's Support Effect is voided.
}}
{{-}}

==153: Thundermon==
{{Card Infobox DDCB-DM
 |name=Thundermon
 |name_jp=サンダーボールモン
 |name_jp_roman=Thunderballmon
 |number=153
 |level=C
 |specialty=Rare
 |hp=710
 |dp=30
 |pp=10
 |c_attack=Thunder Volt
 |c_attack_jp=サンダーボルト
 |c_attack_jp_roman=Thunderbolt
 |c_pow=350
 |t_attack=Thunder Bomber
 |t_attack_jp=サンダーボマー
 |t_attack_jp_roman=
 |t_pow=300
 |x_attack=Intercepting Bomb
 |x_attack_jp=インターセプトボム
 |x_attack_jp_roman=Intercept Bomb
 |x_pow=0
 |x_effect={{button|x}} Counter
 |support=If opponent used {{button|x}}, discard all Cards in opponent's Hand.
}}
{{-}}

==154: PlatinumSukamon==
{{Card Infobox DDCB-DM
 |name=PlatinumSukamon
 |name_jp=プラチナスカモン
 |name_jp_roman=PlatinaSukamon
 |number=154
 |level=C
 |specialty=Rare
 |hp=850
 |dp=40
 |pp=10
 |c_attack=Metal Bomber
 |c_attack_jp=レアメタルウンチ
 |c_attack_jp_roman=Rare Metal Unchi
 |c_pow=240
 |t_attack=Slippery Sludge
 |t_attack_jp=ウンチスライダー
 |t_attack_jp_roman=Unchi Slider
 |t_pow=200
 |x_attack=Metalic Guard
 |x_attack_jp=メタリックガード
 |x_attack_jp_roman=
 |x_pow=100
 |x_effect={{button|c}} to 0
 |support=Move the top Card from Offline Pile to Online Deck.
}}
{{-}}

==155: ShellNumemon==
{{Card Infobox DDCB-DM
 |name=ShellNumemon
 |name_jp=カラツキヌメモン
 |name_jp_roman=KaratukiNumemon
 |number=155
 |level=C
 |specialty=Rare
 |hp=900
 |dp=30
 |pp=10
 |c_attack=Shell's Attack
 |c_attack_jp=シェルズアタック
 |c_attack_jp_roman=
 |c_pow=250
 |t_attack=Pouring Poop
 |t_attack_jp=ウンチレイン
 |t_attack_jp_roman=Unchi Rain
 |t_pow=150
 |x_attack=Mighty Magic
 |x_attack_jp=マイマイオッド
 |x_attack_jp_roman=Maimai Odd
 |x_pow=150
 |x_effect={{button|c}} to 0
 |support=Discard opponent's top DP Card shown in DP Slot.
}}
{{-}}

==156: Nanimon==
{{Card Infobox DDCB-DM
 |name=Nanimon
 |name_jp=ナニモン
 |name_jp_roman=
 |number=156
 |level=C
 |specialty=Rare
 |hp=700
 |dp=30
 |pp=0
 |c_attack=Power Punch
 |c_attack_jp=ウンチダンク
 |c_attack_jp_roman=Unchi Dunk
 |c_pow=390
 |t_attack=Exploding Punch
 |t_attack_jp={{ruby|ＯＹＡＪＩ|おやじ}}パンチ
 |t_attack_jp_roman=OYAJI Punch
 |t_pow=270
 |x_attack=Dark Spell
 |x_attack_jp=デッドワード
 |x_attack_jp_roman=Dead Word
 |x_pow=0
 |x_effect={{button|x}} Counter
 |support=Return all Cards in own Hand to Online Deck and Shuffle.
}}
{{-}}

==157: Numemon==
{{Card Infobox DDCB-DM
 |name=Numemon
 |name_jp=ヌメモン
 |name_jp_roman=
 |number=157
 |level=C
 |specialty=Rare
 |hp=700
 |dp=30
 |pp=10
 |c_attack=Party Time
 |c_attack_jp=ウンチ投げ
 |c_attack_jp_roman=Unchi Nage
 |c_pow=250
 |t_attack=Filth Kick
 |t_attack_jp=エンガチョキック
 |t_attack_jp_roman=Engacho Kick
 |t_pow=250
 |x_attack=Hyper Stink Shot
 |x_attack_jp=超悪臭噴射
 |x_attack_jp_roman=Chou Akushuu Funsha
 |x_pow=100
 |x_effect={{button|x}} to 0
 |support=Discard opponent's 2 top DP Cards in his DP Slot.
}}
{{-}}

==158: Sukamon==
{{Card Infobox DDCB-DM
 |name=Sukamon
 |name_jp=スカモン
 |name_jp_roman=Scumon
 |number=158
 |level=C
 |specialty=Rare
 |hp=600
 |dp=30
 |pp=10
 |c_attack=Poop Blast
 |c_attack_jp=ウンチパラダイス
 |c_attack_jp_roman=Unchi Paradise
 |c_pow=300
 |t_attack=Poop Punch
 |t_attack_jp=ウンチ投げ
 |t_attack_jp_roman=Unchi Nage
 |t_pow=150
 |x_attack=Quick Poop Shot
 |x_attack_jp=高速ウンチ投げ
 |x_attack_jp_roman=Kousoku Unchi Nage
 |x_pow=200
 |x_effect=Jamming
 |support=Discard 1 Card from opponent's Hand at random.
}}
{{-}}

==159: Rockmon==
{{Card Infobox DDCB-DM
 |name=Rockmon
 |name_jp=ゴーレモン
 |name_jp_roman=Golemon
 |number=159
 |level=C
 |specialty=Rare
 |hp=700
 |dp=40
 |pp=10
 |c_attack=Guardian Bomb
 |c_attack_jp=ガーディアンボム
 |c_attack_jp_roman=
 |c_pow=350
 |t_attack=Anti-Digi Beam
 |t_attack_jp=アンチデジビーム
 |t_attack_jp_roman=
 |t_pow=160
 |x_attack=Gigantic Press
 |x_attack_jp=ガルガントプレス
 |x_attack_jp_roman=Gargant Press
 |x_pow=250
 |x_effect=Rare Foe x3
 |support=Discard 3 Cards from opponent's Online Deck.
}}
{{-}}

==160: Geremon==
{{Card Infobox DDCB-DM
 |name=Geremon
 |name_jp=ゲレモン
 |name_jp_roman=
 |number=160
 |level=C
 |specialty=Rare
 |hp=690
 |dp=30
 |pp=10
 |c_attack=Dirty Puddle
 |c_attack_jp=ダーティパトル
 |c_attack_jp_roman=
 |c_pow=280
 |t_attack=Hyper Stink
 |t_attack_jp=ハイパースメル
 |t_attack_jp_roman=
 |t_pow=330
 |x_attack=Polka Dots
 |x_attack_jp=ポルカダッツ
 |x_attack_jp_roman=
 |x_pow=120
 |x_effect=None
 |support=Discard all Cards in DP Slot. Foe discards same number of DP Cards.
}}
{{-}}

==161: NiseDrimogemon==
{{Card Infobox DDCB-DM
 |name=NiseDrimogemon
 |name_jp=ニセドリモゲモン
 |name_jp_roman=
 |number=161
 |level=C
 |specialty=Rare
 |hp=750
 |dp=30
 |pp=10
 |c_attack=Bogus Iron Drill Spin
 |c_attack_jp=ニセドリルスピン
 |c_attack_jp_roman=Nise Drill Spin
 |c_pow=400
 |t_attack=Bogus Bone
 |t_attack_jp=ニセボーン
 |t_attack_jp_roman=Nise Bone
 |t_pow=300
 |x_attack=Fake Special Attack
 |x_attack_jp=ニセスペシャル
 |x_attack_jp_roman=Nise Special
 |x_pow=220
 |x_effect=Rare Foe x3
 |support=Opponent uses {{button|t}}.
}}
{{-}}

==162: ShimaUnimon==
{{Card Infobox DDCB-DM
 |name=ShimaUnimon
 |name_jp=シマユニモン
 |name_jp_roman=
 |number=162
 |level=C
 |specialty=Rare
 |hp=800
 |dp=30
 |pp=10
 |c_attack=Striped Blaster
 |c_attack_jp=ラスターショット
 |c_attack_jp_roman=Luster Shot
 |c_pow=430
 |t_attack=Wild Thunder
 |t_attack_jp=ワイルドサンダー
 |t_attack_jp_roman=
 |t_pow=250
 |x_attack=Mirage Dance
 |x_attack_jp=ミラージュダンス
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=None
}}
{{-}}

==163: MudFrigimon==
{{Card Infobox DDCB-DM
 |name=MudFrigimon
 |name_jp=ツチダルモン
 |name_jp_roman=Tuchidarumon
 |number=163
 |level=C
 |specialty=Rare
 |hp=930
 |dp=30
 |pp=10
 |c_attack=Heavy Punch
 |c_attack_jp=グレートウェイド
 |c_attack_jp_roman=Great Weight
 |c_pow=480
 |t_attack=Mad Rocker
 |t_attack_jp=ロックトゥマッド
 |t_attack_jp_roman=Rock to Mud
 |t_pow=360
 |x_attack=Piece of Earth
 |x_attack_jp=ピースオブアース
 |x_attack_jp_roman=
 |x_pow=320
 |x_effect=None
 |support=None
}}
{{-}}

==164: SandYanmamon==
{{Card Infobox DDCB-DM
 |name=SandYanmamon
 |name_jp=サンドヤンマモン
 |name_jp_roman=
 |number=164
 |level=C
 |specialty=Rare
 |hp=600
 |dp=20
 |pp=10
 |c_attack=Desert Storm
 |c_attack_jp=デザートウィンド
 |c_attack_jp_roman=Desert Wind
 |c_pow=250
 |t_attack=Flying Breaker
 |t_attack_jp=フラインブレイク
 |t_attack_jp_roman=Flying Break
 |t_pow=340
 |x_attack=Bottom Cutter
 |x_attack_jp=ボトムカッター
 |x_attack_jp_roman=
 |x_pow=210
 |x_effect=1st Attack
 |support=Opponent uses {{button|c}}. Lower opponent's Attack Power -100.
}}
{{-}}

==165: L-ToyAgumon==
{{Card Infobox DDCB-DM
 |name=L-ToyAgumon
 |name_jp=トイアグモンL
 |name_jp_roman=ToyAgumon L
 |number=165
 |level=R
 |specialty=Rare
 |hp=590
 |dp=0
 |pp=20
 |c_attack=Toy Flame
 |c_attack_jp=トイフレイム
 |c_attack_jp_roman=
 |c_pow=270
 |t_attack=Million Punches
 |t_attack_jp=マリオンパンチ
 |t_attack_jp_roman=Mullion Punch
 |t_pow=210
 |x_attack=Fancy Star
 |x_attack_jp=ファンシースター
 |x_attack_jp_roman=
 |x_pow=180
 |x_effect=None
 |support=If 1 or less Cards left in own Hand, opponent's Attack Power goes to 0.
}}
{{-}}

==166: Hagurumon==
{{Card Infobox DDCB-DM
 |name=Hagurumon
 |name_jp=ハグルモン
 |name_jp_roman=
 |number=166
 |level=R
 |specialty=Rare
 |hp=500
 |dp=0
 |pp=20
 |c_attack=Darkness Gear
 |c_attack_jp=ダークネスギア
 |c_attack_jp_roman=
 |c_pow=240
 |t_attack=Command Input
 |t_attack_jp=コマンドインプット
 |t_attack_jp_roman=
 |t_pow=200
 |x_attack=Crash Device
 |x_attack_jp=クラッシュデバイス
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect=Crash
 |support=Discard all Cards in DP Slot. Recover HP, mumber of discards x100.
}}
{{-}}

==167: ToyAgumon==
{{Card Infobox DDCB-DM
 |name=ToyAgumon
 |name_jp=トイアグモン
 |name_jp_roman=
 |number=167
 |level=R
 |specialty=Rare
 |hp=530
 |dp=0
 |pp=20
 |c_attack=Toy Flame
 |c_attack_jp=トイフレイム
 |c_attack_jp_roman=
 |c_pow=280
 |t_attack=Million Punches
 |t_attack_jp=マリオンパンチ
 |t_attack_jp_roman=Mullion Punch
 |t_pow=130
 |x_attack=Fancy Star
 |x_attack_jp=ファンシースター
 |x_attack_jp_roman=
 |x_pow=0
 |x_effect={{button|t}} Counter
 |support=Discard 1 Card at random from own Hand. HP of both Players are 200.
}}
{{-}}

==168: ClearAgumon==
{{Card Infobox DDCB-DM
 |name=ClearAgumon
 |name_jp=クリアアグモン
 |name_jp_roman=
 |number=168
 |level=R
 |specialty=Rare
 |hp=580
 |dp=0
 |pp=20
 |c_attack=Precious Flame
 |c_attack_jp=プレシャスフレア
 |c_attack_jp_roman=Precious Flare
 |c_pow=270
 |t_attack=Dream Missile
 |t_attack_jp=ドリームミサイル
 |t_attack_jp_roman=
 |t_pow=220
 |x_attack=Wonder Light
 |x_attack_jp=ワンダーイルミナ
 |x_attack_jp_roman=Wonder Illumina
 |x_pow=50
 |x_effect=Jamming
 |support=Opponent's Support Effect is voided.
}}
{{-}}

==169: Vi-Elecmon==
{{Card Infobox DDCB-DM
 |name=Vi-Elecmon
 |name_jp=エレキモンVi
 |name_jp_roman=Elecmon Vi
 |number=169
 |level=R
 |specialty=Rare
 |hp=620
 |dp=0
 |pp=20
 |c_attack=Jamming Thunder
 |c_attack_jp=ジャミングサンダー
 |c_attack_jp_roman=
 |c_pow=260
 |t_attack=Dark Tail
 |t_attack_jp=テイルダスク
 |t_attack_jp_roman=Tail Dusk
 |t_pow=220
 |x_attack=Assassin Bolt
 |x_attack_jp=アサシンズボルト
 |x_attack_jp_roman=Assassin's Bolt
 |x_pow=190
 |x_effect=Rare Foe x3
 |support=None
}}
{{-}}

==170: Psychemon==
{{Card Infobox DDCB-DM
 |name=Psychemon
 |name_jp=サイケモン
 |name_jp_roman=
 |number=170
 |level=R
 |specialty=Rare
 |hp=470
 |dp=0
 |pp=20
 |c_attack=Colored Sparkle
 |c_attack_jp=カラフルスパーク
 |c_attack_jp_roman=Colorful Spark
 |c_pow=250
 |t_attack=Glittering Horn
 |t_attack_jp=ハデハデホーン
 |t_attack_jp_roman=Hadehade Horn
 |t_pow=120
 |x_attack=Colorful Dance
 |x_attack_jp=原色の舞い
 |x_attack_jp_roman=Gensoku no Mai
 |x_pow=90
 |x_effect={{button|c}} to 0
 |support=Own HP become same as opponent's.
}}
{{-}}

==171: ModokiBetamon==
{{Card Infobox DDCB-DM
 |name=ModokiBetamon
 |name_jp=モドキベタモン
 |name_jp_roman=
 |number=171
 |level=R
 |specialty=Rare
 |hp=550
 |dp=0
 |pp=10
 |c_attack=Electric Shock
 |c_attack_jp=電光ビリリン
 |c_attack_jp_roman=Denkou Biririn
 |c_pow=120
 |t_attack=Blade Fin
 |t_attack_jp=ブレードフィン
 |t_attack_jp_roman=
 |t_pow=280
 |x_attack=Aqua Tower
 |x_attack_jp=アクアタワー
 |x_attack_jp_roman=
 |x_pow=190
 |x_effect={{button|c}} to 0
 |support=Opponent's HP become same as own. Own Attack Power becomes 0.
}}
{{-}}

==172: Flamedramon==
{{Card Infobox DDCB-DM
 |name=Flamedramon
 |name_jp=フレイドラモン
 |name_jp_roman=
 |number=172
 |level=A
 |specialty=Fire
 |hp=600
 |dp=0
 |pp=0
 |c_attack=Fire Rocket
 |c_attack_jp=ファイアロケット
 |c_attack_jp_roman=
 |c_pow=500
 |t_attack=Knuckle Fire
 |t_attack_jp=ナックルファイア
 |t_attack_jp_roman=
 |t_pow=350
 |x_attack=Express Claw
 |x_attack_jp=クローエクスプレス
 |x_attack_jp_roman=Claw Express
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=Boost own Attack Power +100. Draw 1 Card.
}}
{{-}}

==173: Magnamon==
{{Card Infobox DDCB-DM
 |name=Magnamon
 |name_jp=マグナモン
 |name_jp_roman=
 |number=173
 |level=A
 |specialty=Fire
 |hp=650
 |dp=0
 |pp=0
 |c_attack=Plasma Shot
 |c_attack_jp=
 |c_attack_jp_roman=
 |c_pow=550
 |t_attack=Plasma Blast
 |t_attack_jp=
 |t_attack_jp_roman=
 |t_pow=300
 |x_attack=Aura Barrier
 |x_attack_jp=
 |x_attack_jp_roman=
 |x_pow=200
 |x_effect={{button|c}} to 0
 |support=Boost own Attack Power by +100. Draw 1 Card.
}}
{{-}}

==174: Baronmon==
{{Card Infobox DDCB-DM
 |name=Baronmon
 |name_jp=バロモン
 |name_jp_roman=Baromon
 |number=174
 |level=A
 |specialty=Fire
 |hp=600
 |dp=0
 |pp=0
 |c_attack=Dancing Meteor
 |c_attack_jp=メテオダンス
 |c_attack_jp_roman=Meteor Dance
 |c_pow=550
 |t_attack=Pyrokinesis
 |t_attack_jp=パイロキネシス
 |t_attack_jp_roman=
 |t_pow=450
 |x_attack=White Spell
 |x_attack_jp=ホワイトスペル
 |x_attack_jp_roman=
 |x_pow=150
 |x_effect={{button|c}} to 0
 |support=If foe's Specialty is Darkness, own Attack Power is Doubled. Draw 1 Card.
}}
{{-}}

==175: Veemon==
{{Card Infobox DDCB-DM
 |name=Veemon
 |name_jp=ブイモン
 |name_jp_roman=V-mon
 |number=175
 |level=R <sub>P</sub>
 |specialty=Fire
 |hp=550
 |dp=0
 |pp=20
 |c_attack=Vee Head Butt
 |c_attack_jp=ブイモンヘッド
 |c_attack_jp_roman=V-mon Head
 |c_pow=350
 |t_attack=Boom Boom Punch
 |t_attack_jp=ブンブンパンチ
 |t_attack_jp_roman=Bunbun Punch
 |t_pow=280
 |x_attack=Hopping Kick
 |x_attack_jp=ホッピングキック
 |x_attack_jp_roman=
 |x_pow=200
 |x_effect=None
 |support=Boost own Attack Power +100. Draw 1 Card.
}}
{{-}}

==176: Submarimon==
{{Card Infobox DDCB-DM
 |name=Submarimon
 |name_jp=サブマリモン
 |name_jp_roman=Sabmarimon
 |number=176
 |level=A
 |specialty=Ice
 |hp=850
 |dp=0
 |pp=0
 |c_attack=Submarine Attack
 |c_attack_jp=サブマリンアタック
 |c_attack_jp_roman=
 |c_pow=400
 |t_attack=Hydro Jet
 |t_attack_jp=ハイドロジェット
 |t_attack_jp_roman=
 |t_pow=300
 |x_attack=OXY Homing Missile
 |x_attack_jp={{ruby|ＯＸＧ|オキシゲン}}ホーミング
 |x_attack_jp_roman=Oxygen Homing
 |x_pow=200
 |x_effect={{button|c}} to 0
 |support=Discard 2 Cards from opponent's Online Deck. Draw 1 Card.
}}
{{-}}

==177: Quetzalmon==
{{Card Infobox DDCB-DM
 |name=Quetzalmon
 |name_jp=クアトルモン
 |name_jp_roman=
 |number=177
 |level=A
 |specialty=Ice
 |hp=800
 |dp=0
 |pp=0
 |c_attack=Freezing Wave
 |c_attack_jp=フリーズウェーブ
 |c_attack_jp_roman=Freeze Wave
 |c_pow=400
 |t_attack=Toltec Wind
 |t_attack_jp=トルテカンウインド
 |t_attack_jp_roman=Toltecan Wind
 |t_pow=350
 |x_attack=Cold and Clammy
 |x_attack_jp=デッドオアアライブ
 |x_attack_jp_roman=Dead or Alive
 |x_pow=0
 |x_effect={{button|x}} Counter
 |support=Lower Opponent's Attack Power -100. Draw 1 Card.
}}
{{-}}

==178: Tylomon==
{{Card Infobox DDCB-DM
 |name=Tylomon
 |name_jp=ティロモン
 |name_jp_roman=
 |number=178
 |level=A
 |specialty=Ice
 |hp=900
 |dp=0
 |pp=0
 |c_attack=Torpedo Attack
 |c_attack_jp=トーピードアタック
 |c_attack_jp_roman=
 |c_pow=350
 |t_attack=Heavy Anchor
 |t_attack_jp=ティルトアンカー
 |t_attack_jp_roman=Tilt Anchor
 |t_pow=300
 |x_attack=Eraser Beam
 |x_attack_jp=イレイザービロウ
 |x_attack_jp_roman=Eraser Below
 |x_pow=250
 |x_effect=Fire Foe x3
 |support=Change own Specialty to Nature. Draw 1 Card.
}}
{{-}}

==179: Halsemon==
{{Card Infobox DDCB-DM
 |name=Halsemon
 |name_jp=ホルスモン
 |name_jp_roman=Holsmon
 |number=179
 |level=A
 |specialty=Nature
 |hp=700
 |dp=0
 |pp=0
 |c_attack=Tempest Wing
 |c_attack_jp=テンペストウィング
 |c_attack_jp_roman=
 |c_pow=400
 |t_attack=Red Sun
 |t_attack_jp=レッドサン
 |t_attack_jp_roman=
 |t_pow=300
 |x_attack=Evil Gaze
 |x_attack_jp=ウジャトゲイズ
 |x_attack_jp_roman=Udjat Gaze
 |x_pow=250
 |x_effect={{button|c}} to 0
 |support=Draw 3 Cards.
}}
{{-}}

==180: Pegasusmon==
{{Card Infobox DDCB-DM
 |name=Pegasusmon
 |name_jp=ペガスモン
 |name_jp_roman=Pegasmon
 |number=180
 |level=A
 |specialty=Nature
 |hp=750
 |dp=0
 |pp=0
 |c_attack=Star Shower
 |c_attack_jp=シューティングスター
 |c_attack_jp_roman=Shooting Star
 |c_pow=400
 |t_attack=Rodeo Kick
 |t_attack_jp=ロデオギャロップ
 |t_attack_jp_roman=Rodeo Gallop
 |t_pow=300
 |x_attack=Needle Rain
 |x_attack_jp=ニードルレイン
 |x_attack_jp_roman=
 |x_pow=200
 |x_effect=1st Attack
 |support=If foe's Specialty is Nature, own Attack Power is doubled. Draw 1 Card.
}}
{{-}}

==181: Nefertimon==
{{Card Infobox DDCB-DM
 |name=Nefertimon
 |name_jp=ネフェルティモン
 |name_jp_roman=
 |number=181
 |level=A
 |specialty=Nature
 |hp=650
 |dp=0
 |pp=0
 |c_attack=Rocking Stone
 |c_attack_jp=ロゼッタストーン
 |c_attack_jp_roman=Rosetta Stone
 |c_pow=500
 |t_attack=Egyptian Fire
 |t_attack_jp=ナイルジュエリー
 |t_attack_jp_roman=Nile Jewelry
 |t_pow=300
 |x_attack=Queen's Curse
 |x_attack_jp=カースオブクイーン
 |x_attack_jp_roman=Curse of Queen
 |x_pow=200
 |x_effect={{button|c}} to 0
 |support=Change own Specialty to Nature. Draw 1 card.
}}
{{-}}

==182: Hawkmon==
{{Card Infobox DDCB-DM
 |name=Hawkmon
 |name_jp=ホークモン
 |name_jp_roman=
 |number=182
 |level=R <sub>P</sub>
 |specialty=Nature
 |hp=600
 |dp=0
 |pp=30
 |c_attack=Hawk Beam
 |c_attack_jp=フェザースラッシュ
 |c_attack_jp_roman=Feather Slash
 |c_pow=300
 |t_attack=Pecking Beak
 |t_attack_jp=ビークペッカー
 |t_attack_jp_roman=Beak Pecker
 |t_pow=220
 |x_attack=Hawk Claw
 |x_attack_jp=ループザホーク
 |x_attack_jp_roman=Loop the Hawk
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=Draw 3 Cards.
}}
{{-}}

==183: Patamon==
{{Card Infobox DDCB-DM
 |name=Patamon
 |name_jp=パタモン
 |name_jp_roman=
 |number=183
 |level=R <sub>P</sub>
 |specialty=Nature
 |hp=630
 |dp=0
 |pp=30
 |c_attack=Boom Bubble
 |c_attack_jp=エアショット
 |c_attack_jp_roman=Air Shot
 |c_pow=370
 |t_attack=Pretty Attack
 |t_attack_jp=プリティラッシュ
 |t_attack_jp_roman=Pretty Rush
 |t_pow=170
 |x_attack=Intercepting Air Shot
 |x_attack_jp=迎撃エアショット
 |x_attack_jp_roman=Geigeki Air Shot
 |x_pow=0
 |x_effect={{button|c}} Counter
 |support=If foe's Specialty is Darkness, own Attack Power is doubled. Draw 1 Card.
}}
{{-}}

==184: Gatomon==
{{Card Infobox DDCB-DM
 |name=Gatomon
 |name_jp=テイルモン
 |name_jp_roman=Tailmon
 |number=184
 |level=R <sub>P</sub>
 |specialty=Nature
 |hp=600
 |dp=0
 |pp=30
 |c_attack=Lightning Paw
 |c_attack_jp=ネコパンチ
 |c_attack_jp_roman=Neko Punch
 |c_pow=290
 |t_attack=Lightning Kick
 |t_attack_jp=ネコキック
 |t_attack_jp_roman=Neko Kick
 |t_pow=200
 |x_attack=Cat's Eyes
 |x_attack_jp=キャッツ・アイ
 |x_attack_jp_roman=Cat's Eye
 |x_pow=0
 |x_effect={{button|t}} Counter
 |support=Change own Specialty to Nature. Draw 1 Card.
}}
{{-}}

==185: Raidramon==
{{Card Infobox DDCB-DM
 |name=Raidramon
 |name_jp=ライドラモン
 |name_jp_roman=Lighdramon
 |number=185
 |level=A
 |specialty=Darkness
 |hp=650
 |dp=0
 |pp=0
 |c_attack=Lightning Blast
 |c_attack_jp=ブルーサンダー
 |c_attack_jp_roman=Blue Thunder
 |c_pow=300
 |t_attack=Electric Byte
 |t_attack_jp=エレクトリックバイト
 |t_attack_jp_roman=Electric Bite
 |t_pow=300
 |x_attack=Lightning Blade
 |x_attack_jp=ライトニングブレード
 |x_attack_jp_roman=
 |x_pow=400
 |x_effect={{button|t}} to 0
 |support=Boost own Attack Power by +100. Draw 1 Card.
}}
{{-}}

==186: Shadramon==
{{Card Infobox DDCB-DM
 |name=Shadramon
 |name_jp=シェイドラモン
 |name_jp_roman=
 |number=186
 |level=A
 |specialty=Darkness
 |hp=650
 |dp=0
 |pp=0
 |c_attack=Flare Buster
 |c_attack_jp=フレアバスター
 |c_attack_jp_roman=
 |c_pow=500
 |t_attack=Serrated Screw
 |t_attack_jp=インデントスクリュー
 |t_attack_jp_roman=Indent Screw
 |t_pow=350
 |x_attack=Psychic Wave
 |x_attack_jp=サイキックウェーブ
 |x_attack_jp_roman=
 |x_pow=150
 |x_effect=Jamming
 |support=Lower Opponent's Attack Power -100. Draw 1 Card.
}}
{{-}}

==187: Wormmon==
{{Card Infobox DDCB-DM
 |name=Wormmon
 |name_jp=ワームモン
 |name_jp_roman=
 |number=187
 |level=R <sub>P</sub>
 |specialty=Darkness
 |hp=550
 |dp=0
 |pp=20
 |c_attack=Sticky Net
 |c_attack_jp=ネバネバネット
 |c_attack_jp_roman=Nebaneba Net
 |c_pow=300
 |t_attack=Silk Thread
 |t_attack_jp=シルクスレッド
 |t_attack_jp_roman=
 |t_pow=250
 |x_attack=Random Roll
 |x_attack_jp=ランダンロール
 |x_attack_jp_roman=
 |x_pow=170
 |x_effect={{button|c}} to 0
 |support=Lower Opponent's Attack Power -100. Draw 1 Card.
}}
{{-}}

==188: Shurimon==
{{Card Infobox DDCB-DM
 |name=Shurimon
 |name_jp=シュリモン
 |name_jp_roman=
 |number=188
 |level=A
 |specialty=Rare
 |hp=600
 |dp=0
 |pp=0
 |c_attack=Double Stars
 |c_attack_jp=クサナギ
 |c_attack_jp_roman=Kusanagi
 |c_pow=450
 |t_attack=Burning Chili Pepper
 |t_attack_jp=紅葉おろし
 |t_attack_jp_roman=Momiji Oroshi
 |t_pow=350
 |x_attack=Jumping Drill
 |x_attack_jp=テンドリルジャンプ
 |x_attack_jp_roman=Tendril Jump
 |x_pow=250
 |x_effect={{button|x}} to 0
 |support=Draw 3 Cards.
}}
{{-}}

==189: Digmon==
{{Card Infobox DDCB-DM
 |name=Digmon
 |name_jp=ディグモン
 |name_jp_roman=
 |number=189
 |level=A
 |specialty=Rare
 |hp=800
 |dp=0
 |pp=0
 |c_attack=Gold Rush
 |c_attack_jp=ゴールドラッシュ
 |c_attack_jp_roman=
 |c_pow=400
 |t_attack=Powerful Cracker
 |t_attack_jp=ビッグクラック
 |t_attack_jp_roman=Big Crack
 |t_pow=400
 |x_attack=Titanic Drill
 |x_attack_jp=タイタンドリル
 |x_attack_jp_roman=Titan Drill
 |x_pow=400
 |x_effect=None
 |support=Discard 2 Cards from opponent's Online Deck. Draw 1 Card.
}}
{{-}}

==190: Armadillomon==
{{Card Infobox DDCB-DM
 |name=Armadillomon
 |name_jp=アルマジモン
 |name_jp_roman=Armadimon
 |number=190
 |level=R <sub>P</sub>
 |specialty=Rare
 |hp=650
 |dp=0
 |pp=20
 |c_attack=Diamond Shell
 |c_attack_jp=ローリングストーン
 |c_attack_jp_roman=Rolling Stone
 |c_pow=280
 |t_attack=Beat Blaster
 |t_attack_jp=スクラッチビート
 |t_attack_jp_roman=Scratch Beat
 |t_pow=240
 |x_attack=Hard Brick
 |x_attack_jp=リジッドブロック
 |x_attack_jp_roman=Rigid Block
 |x_pow=190
 |x_effect={{button|c}} to 0
 |support=Discard 2 Cards from opponent's Online Deck. Draw 1 Card.
}}
{{-}}

==191: Golden Banana==
{{Card Infobox DDCB-DM
 |name=Golden Banana
 |name_jp=金のバナナ
 |name_jp_roman=Kin no Banana
 |number=191
 |effect=Own HP are halved. Counterattack. Attack second.
}}
{{-}}

==192: Devil's Chip==
{{Card Infobox DDCB-DM
 |name=Devil's Chip
 |name_jp=デビルチップ
 |name_jp_roman=Devil Chip
 |number=192
 |effect=Discard 1 Card from own Hand. Boost both players' Attack Power +600.
}}
{{-}}

==193: Whistle==
{{Card Infobox DDCB-DM
 |name=Whistle
 |name_jp=ホイッスル
 |name_jp_roman=
 |number=193
 |effect=If own Level is below opponent's, opponent's Attack Power becomes 0.
}}
{{-}}

==194: Giga Hand==
{{Card Infobox DDCB-DM
 |name=Giga Hand
 |name_jp=ギガハンド
 |name_jp_roman=
 |number=194
 |effect=Discard 7 Cards from Online Deck. Own Attack Power is same as own HP.
}}
{{-}}

==195: Metallic Banana==
{{Card Infobox DDCB-DM
 |name=Metallic Banana
 |name_jp=メタルバナナ
 |name_jp_roman=Metal Banana
 |number=195
 |effect=Own HP are halved. Opponent's Attack Power becomes 0.
}}
{{-}}

==196: Shining Mane==
{{Card Infobox DDCB-DM
 |name=Shining Mane
 |name_jp=輝くたてがみ
 |name_jp_roman=Kagayaku Tategami
 |number=196
 |effect=If opponent's HP are more than 1000, opponent's HP are halved.
}}
{{-}}

==197: Mega Rec. Floppy==
{{Card Infobox DDCB-DM
 |name=Mega Rec. Floppy
 |name_jp=超回復フロッピー
 |name_jp_roman=Choukaifuku Floppy
 |number=197
 |effect=Discard 7 Cards from own Online Deck. Recover own HP by +1000.
}}
{{-}}

==198: Mega Attack Chip==
{{Card Infobox DDCB-DM
 |name=Mega Attack Chip
 |name_jp=超攻撃チップ
 |name_jp_roman=Choukougeki Chip
 |number=198
 |effect=Discard 7 Cards from own Online Deck. Boost own Attack Power +500.
}}
{{-}}

==199: Dark Lord's Cape==
{{Card Infobox DDCB-DM
 |name=Dark Lord's Cape
 |name_jp=闇貴族のマント
 |name_jp_roman=Yami Kizoku no Mantle
 |number=199
 |effect=If opponent's HP is less than own, boost own Attack Power +400.
}}
{{-}}

==200: Fake Sevens==
{{Card Infobox DDCB-DM
 |name=Fake Sevens
 |name_jp=にせセブンズ
 |name_jp_roman=Nise Sevens
 |number=200
 |effect=None
}}
{{-}}

==201: Net Worm==
{{Card Infobox DDCB-DM
 |name=Net Worm
 |name_jp=ネットワーム
 |name_jp_roman=
 |number=201
 |effect=If both players use same Attack, discard all Cards in foe's Hand.
}}
{{-}}

==202: Missile Pod==
{{Card Infobox DDCB-DM
 |name=Missile Pod
 |name_jp=ミサイルポッド
 |name_jp_roman=
 |number=202
 |effect=Discard all Cards in own Hand. Own Attack Power is doubled.
}}
{{-}}

==203: Shogun's Order==
{{Card Infobox DDCB-DM
 |name=Shogun's Order
 |name_jp=トノサマのおふれ
 |name_jp_roman=Tonosama no Ofure
 |number=203
 |effect=Both players' Attack Power becomes 0.
}}
{{-}}

==204: Beetle Diamond==
{{Card Infobox DDCB-DM
 |name=Beetle Diamond
 |name_jp=ビートルダイヤ
 |name_jp_roman=Beetle Dia
 |number=204
 |effect=Attack first. Boost own Attack Power +100.
}}
{{-}}

==205: Dark Bone==
{{Card Infobox DDCB-DM
 |name=Dark Bone
 |name_jp=死を呼ぶ骨
 |name_jp_roman=Shi wo Yobu Hone
 |number=205
 |effect=Own attack becomes "Eat-up HP."
}}
{{-}}

==206: Red Digivice==
{{Card Infobox DDCB-DM
 |name=Red Digivice
 |name_jp=レッドデジヴァイス
 |name_jp_roman=
 |number=206
 |effect=If own Specialty is Fire, boost own Attack Power +100, recover HP +200.
}}
{{-}}

==207: Blue Digivice==
{{Card Infobox DDCB-DM
 |name=Blue Digivice
 |name_jp=ブルーデジヴァイス
 |name_jp_roman=
 |number=207
 |effect=If own Specialty is Ice, boost own Attack Power +100, recover HP +200.
}}
{{-}}

==208: Green Digivice==
{{Card Infobox DDCB-DM
 |name=Green Digivice
 |name_jp=グリーンデジヴァイス
 |name_jp_roman=
 |number=208
 |effect=If own Specialty is Nature, boost own Attack Power +100, recover HP +200.
}}
{{-}}

==209: Black Digivice==
{{Card Infobox DDCB-DM
 |name=Black Digivice
 |name_jp=ブラックデジヴァイス
 |name_jp_roman=
 |number=209
 |effect=If own Specialty is Darkness, boost own Attack Power +100, recover HP +200.
}}
{{-}}

==210: Yellow Digivice==
{{Card Infobox DDCB-DM
 |name=Yellow Digivice
 |name_jp=イエローデジヴァイス
 |name_jp_roman=
 |number=210
 |effect=If own Specialty is Rare, boost own Attack Power +100, recover HP +200.
}}
{{-}}

==211: Pink Digivice==
{{Card Infobox DDCB-DM
 |name=Pink Digivice
 |name_jp=ピンクデジヴァイス
 |name_jp_roman=
 |number=211
 |effect=If Specialties are same, boost own Attack Power +200, recover HP +400.
}}
{{-}}

==212: Another Dimension==
{{Card Infobox DDCB-DM
 |name=Another Dimension
 |name_jp=裏次元
 |name_jp_roman=Urajigen
 |number=212
 |effect=Discard 7 Cards from both players' Online Decks.
}}
{{-}}

==213: UnInstall==
{{Card Infobox DDCB-DM
 |name=UnInstall
 |name_jp=アンインストール
 |name_jp_roman=
 |number=213
 |effect=If both Attacks are same, discard 7 Cards from foe's Online Deck.
}}
{{-}}

==214: Evil Program==
{{Card Infobox DDCB-DM
 |name=Evil Program
 |name_jp=不幸のプログラム
 |name_jp_roman=Fukou no Program
 |number=214
 |effect=Discard 1 Card in own DP Slot. Discard all foe's Cards in DP Slot.
}}
{{-}}

==215: Coliseum==
{{Card Infobox DDCB-DM
 |name=Coliseum
 |name_jp=コロシアム
 |name_jp_roman=
 |number=215
 |effect=Both players' attacks become {{button|c}}. Boost own {{button|c}} Attack Power +100.
}}
{{-}}

==216: Fire Altar==
{{Card Infobox DDCB-DM
 |name=Fire Altar
 |name_jp=火炎の祭だん
 |name_jp_roman=Kaen no Saidan
 |number=216
 |effect=Changes opponent's Specialty to Fire. Draw 1 Card from own Online Deck.
}}
{{-}}

==217: Ice Altar==
{{Card Infobox DDCB-DM
 |name=Ice Altar
 |name_jp=氷水の祭だん
 |name_jp_roman=Koorimizu no Saidan
 |number=217
 |effect=Changes opponent's Specialty to Ice. Draw 1 Card from own Online Deck.
}}
{{-}}

==218: Nature Altar==
{{Card Infobox DDCB-DM
 |name=Nature Altar
 |name_jp=自然の祭だん
 |name_jp_roman=Shizen no Saidan
 |number=218
 |effect=Changes opponent's Specialty to Nature. Draw 1 Card from own Online Deck.
}}
{{-}}

==219: Darkness Altar==
{{Card Infobox DDCB-DM
 |name=Darkness Altar
 |name_jp=暗黒の祭だん
 |name_jp_roman=Ankoku no Saidan
 |number=219
 |effect=Changes opponent's Specialty to Darkness. Draw 1 Card from own Online Deck.
}}
{{-}}

==220: Rare Altar==
{{Card Infobox DDCB-DM
 |name=Rare Altar
 |name_jp=珍種の祭だん
 |name_jp_roman=Chinshu no Saidan
 |number=220
 |effect=Changes opponent's Specialty to Rare. Draw 1 Card from own Online Deck.
}}
{{-}}

==221: Sup. Rec. Floppy==
{{Card Infobox DDCB-DM
 |name=Sup. Rec. Floppy
 |name_jp=大回復フロッピー
 |name_jp_roman=Daikaifuku Floppy
 |number=221
 |effect=If own HP are less than foe's HP, recovcer own HP by +700.
}}
{{-}}

==222: Mega Def. Disk {{button|c}}==
{{Card Infobox DDCB-DM
 |name=Mega Def. Disk {{button|c}}
 |name_jp=超防御プラグイン○
 |name_jp_roman=Choubougyo Plugin ○
 |filename=Mega Def. Disk ○
 |number=222
 |effect=Opponent's {{button|c}} Attack Power goes to 0. Recover own HP by +100.
}}
{{-}}

==223: Mega Def. Disk {{button|t}}==
{{Card Infobox DDCB-DM
 |name=Mega Def. Disk {{button|t}}
 |name_jp=超防御プラグイン△
 |name_jp_roman=Choubougyo Plugin △
 |filename=Mega Def. Disk △
 |number=223
 |effect=Opponent's {{button|t}} Attack Power goes to 0. Recover own HP by +100.
}}
{{-}}

==224: Mega Def. Disk {{button|x}}==
{{Card Infobox DDCB-DM
 |name=Mega Def. Disk {{button|x}}
 |name_jp=超防御プラグイン×
 |name_jp_roman=Choubougyo Plugin ×
 |filename=Mega Def. Disk ×
 |number=224
 |effect=Opponent's {{button|x}} Attack Power goes to 0. Recover own HP by +100.
}}
{{-}}

==225: Heap of Junk==
{{Card Infobox DDCB-DM
 |name=Heap of Junk
 |name_jp=ゴミの山
 |name_jp_roman=Gomi no Yama
 |number=225
 |effect=Opponent discards 2 Cards from his Online Deck and 1 Card from Hand.
}}
{{-}}

==226: Beam Gun==
{{Card Infobox DDCB-DM
 |name=Beam Gun
 |name_jp=ビームガン
 |name_jp_roman=
 |number=226
 |effect=Own Attack Power becomes 0. Opponent's HP are halved.
}}
{{-}}

==227: Chain Saw==
{{Card Infobox DDCB-DM
 |name=Chain Saw
 |name_jp=チェンソー
 |name_jp_roman=
 |number=227
 |effect=Make own HP 10. Own Attack Power is tripled.
}}
{{-}}

==228: Metal Parts==
{{Card Infobox DDCB-DM
 |name=Metal Parts
 |name_jp=メタルパーツ
 |name_jp_roman=
 |number=228
 |effect=Discard own Hand. Multiply own Attack Power by number of discarded Cards.
}}
{{-}}

==229: Metal Armor==
{{Card Infobox DDCB-DM
 |name=Metal Armor
 |name_jp=メタルアーマー
 |name_jp_roman=
 |number=229
 |effect=Discard own DP Slot Cards. Multiply own Attack Power by number of discards.
}}
{{-}}

==230: Mega Hand==
{{Card Infobox DDCB-DM
 |name=Mega Hand
 |name_jp=メガハンド
 |name_jp_roman=
 |number=230
 |effect=Own Attack Power matches own HP, then own HP are halved.
}}
{{-}}

==231: Level Balancer==
{{Card Infobox DDCB-DM
 |name=Level Balancer
 |name_jp=レベルバランサー
 |name_jp_roman=
 |number=231
 |effect=If own Level is R, boost own Attack Power +400.
}}
{{-}}

==232: Level Manager==
{{Card Infobox DDCB-DM
 |name=Level Manager
 |name_jp=レベルマネージャー
 |name_jp_roman=
 |number=232
 |effect=If own Level is C, boost own Attack Power +400.
}}
{{-}}

==233: Level Booster==
{{Card Infobox DDCB-DM
 |name=Level Booster
 |name_jp=レベルブースター
 |name_jp_roman=
 |number=233
 |effect=If own Level is U, boost own Attack Power +400.
}}
{{-}}

==234: Armor Clash==
{{Card Infobox DDCB-DM
 |name=Armor Clash
 |name_jp=アーマークラッシュ
 |name_jp_roman=
 |number=234
 |effect=If opponent is Level A, his Atk Pwr becomes 0 and own Atk Pwr is doubled.
}}
{{-}}

==235: Silver Ball==
{{Card Infobox DDCB-DM
 |name=Silver Ball
 |name_jp=銀玉
 |name_jp_roman=Gindama
 |number=235
 |effect=If opponent is Level U, his Atk Pwr becomes 0 and own Atk Pwr is doubled.
}}
{{-}}

==236: Coral Charm==
{{Card Infobox DDCB-DM
 |name=Coral Charm
 |name_jp=サンゴのお守り
 |name_jp_roman=Sango no Omamori
 |number=236
 |effect=If foe's Specialty is Fire or Ice, his Attack Power goes to 0.
}}
{{-}}

==237: Patch of Love==
{{Card Infobox DDCB-DM
 |name=Patch of Love
 |name_jp=愛のばんそうこう
 |name_jp_roman=Ai no Bansoukou
 |number=237
 |effect=If foe's Specialty is Nature or Darkness, his Attack Power goes to 0.
}}
{{-}}

==238: Mystery Egg==
{{Card Infobox DDCB-DM
 |name=Mystery Egg
 |name_jp=謎のタマゴ
 |name_jp_roman=Nazo no Tamago
 |number=238
 |effect=Changes both players' Specialties to Rare.
}}
{{-}}

==239: Miracle Ruby==
{{Card Infobox DDCB-DM
 |name=Miracle Ruby
 |name_jp=奇跡のルビー
 |name_jp_roman=Kiseki no Ruby
 |number=239
 |effect=KO'd Digimon revives with 1000. Battle is still lost.
}}
{{-}}

==240: Cyber Parts==
{{Card Infobox DDCB-DM
 |name=Cyber Parts
 |name_jp=サイバーパーツ
 |name_jp_roman=
 |number=240
 |effect=If both Attacks are same, own Attack Power is tripled.
}}
{{-}}

==241: Liquid Crystal==
{{Card Infobox DDCB-DM
 |name=Liquid Crystal
 |name_jp=液晶化
 |name_jp_roman=Ekishouka
 |number=241
 |effect=If both players use same attack, opponent's Attack Power becomes 0.
}}
{{-}}

==242: Deluxe Mushroom==
{{Card Infobox DDCB-DM
 |name=Deluxe Mushroom
 |name_jp=デラックスキノコ
 |name_jp_roman=Deluxe Kinoko
 |number=242
 |effect=If both players use same Attack, recover own HP +700.
}}
{{-}}

==243: Lucky Mushroom==
{{Card Infobox DDCB-DM
 |name=Lucky Mushroom
 |name_jp=運だめしキノコ
 |name_jp_roman=Undameshi Kinoko
 |number=243
 |effect=If both Attacks are different, recover own HP by +500.
}}
{{-}}

==244: Premium Steak==
{{Card Infobox DDCB-DM
 |name=Premium Steak
 |name_jp=極上肉
 |name_jp_roman=Gokujouniku
 |number=244
 |effect=Recover own HP by +500. Recover foe's HP by +200.
}}
{{-}}

==245: Short Lance==
{{Card Infobox DDCB-DM
 |name=Short Lance
 |name_jp=小さな槍
 |name_jp_roman=Chisana Yari
 |number=245
 |effect=If both attacks are different, own Attack Power is doubled.
}}
{{-}}

==246: Med. Rec. Floppy==
{{Card Infobox DDCB-DM
 |name=Med. Rec. Floppy
 |name_jp=中回復フロッピー
 |name_jp_roman=Nakakaifuku Floppy
 |number=246
 |effect=Own Attack Power is halved. Recover own HP by +500.
}}
{{-}}

==247: Digimon Analyzer==
{{Card Infobox DDCB-DM
 |name=Digimon Analyzer
 |name_jp=デジモンアナライザー
 |name_jp_roman=
 |number=247
 |effect=Move top 3 Cards from Offline Pile to Online Deck and shuffle.
}}
{{-}}

==248: Training Manual==
{{Card Infobox DDCB-DM
 |name=Training Manual
 |name_jp=トレーマニュアル
 |name_jp_roman=
 |number=248
 |effect=Draw until there are 4 Cards in own Hand. Recover own HP by +100.
}}
{{-}}

==249: Circle Hitter==
{{Card Infobox DDCB-DM
 |name=Circle Hitter
 |name_jp=サークルキラー
 |name_jp_roman=Circle Killer
 |number=249
 |effect=If opponent uses {{button|c}}, attack first and boost own Attack Power +500.
}}
{{-}}

==250: Triangle Hitter==
{{Card Infobox DDCB-DM
 |name=Triangle Hitter
 |name_jp=トライキラー
 |name_jp_roman=Tri Killer
 |number=250
 |effect=If opponent uses {{button|t}}, attack first and boost own Attack Power +500.
}}
{{-}}

==251: Cross Hitter==
{{Card Infobox DDCB-DM
 |name=Cross Hitter
 |name_jp=クロスキラー
 |name_jp_roman=Cross Killer
 |number=251
 |effect=If opponent uses {{button|x}}, attack first and boost own Attack Power +500.
}}
{{-}}

==252: Suka's Curse==
{{Card Infobox DDCB-DM
 |name=Suka's Curse
 |name_jp=スカの呪い
 |name_jp_roman=Scu no Noroi
 |number=252
 |effect=Opponent discards 2 Cards at random from his Hand.
}}
{{-}}

==253: Cherrymon's Mist==
{{Card Infobox DDCB-DM
 |name=Cherrymon's Mist
 |name_jp=ジュレイモンの霧
 |name_jp_roman=Jyureimon no Kiri
 |number=253
 |effect=Opponent's Support and Option Effects are voided.
}}
{{-}}

==254: Hacking==
{{Card Infobox DDCB-DM
 |name=Hacking
 |name_jp=ハッキング
 |name_jp_roman=
 |number=254
 |effect=If own Level is lower, switch HP with opponent.
}}
{{-}}

==255: Digimon Grave==
{{Card Infobox DDCB-DM
 |name=Digimon Grave
 |name_jp=デジモン墓場
 |name_jp_roman=Digimon Hakaba
 |number=255
 |effect=Opponent discards 4 top Cards from Online Deck.
}}
{{-}}

==256: Data Copy==
{{Card Infobox DDCB-DM
 |name=Data Copy
 |name_jp=データコピー
 |name_jp_roman=
 |number=256
 |effect=Own Attack Power, HP, and Specialty become same as the opponent's.
}}
{{-}}

==257: Partner Finder==
{{Card Infobox DDCB-DM
 |name=Partner Finder
 |name_jp=パートナーサーチャー
 |name_jp_roman=Partner Searcher
 |number=257
 |effect=Pick Partner Card from own Online Deck at random and put in own Hand.
}}
{{-}}

==258: Fire Spot==
{{Card Infobox DDCB-DM
 |name=Fire Spot
 |name_jp=炎のかけら
 |name_jp_roman=Honoo no Kakera
 |number=258
 |effect=Change own Specialty to Fire. Boost own Attack Power +200.
}}
{{-}}

==259: Ice Crystal==
{{Card Infobox DDCB-DM
 |name=Ice Crystal
 |name_jp=氷水晶
 |name_jp_roman=Koorimizushou
 |number=259
 |effect=Change own Specialty to Ice. Recover own HP by +200.
}}
{{-}}

==260: Earth Charm==
{{Card Infobox DDCB-DM
 |name=Earth Charm
 |name_jp=大地のお守り
 |name_jp_roman=Daichi no Omamori
 |number=260
 |effect=Change own Specialty to Nature. Attack first.
}}
{{-}}

==261: Black Gear==
{{Card Infobox DDCB-DM
 |name=Black Gear
 |name_jp=黒い歯車
 |name_jp_roman=Kuroi Haguruma
 |number=261
 |effect=Change own Specialty to Darkness. Both players' HP are halved.
}}
{{-}}

==262: Stuffed Animal==
{{Card Infobox DDCB-DM
 |name=Stuffed Animal
 |name_jp=ぬいぐるみ
 |name_jp_roman=Nuigurumi
 |number=262
 |effect=Change own Specialty to Rare. Opponent discards 1 Card at random.
}}
{{-}}

==263: Disrupt Ray==
{{Card Infobox DDCB-DM
 |name=Disrupt Ray
 |name_jp=混乱電波
 |name_jp_roman=Konrandenpa
 |number=263
 |effect=Opponent's attack changes from {{button|c}} to {{button|t}}, {{button|t}} to {{button|x}}, or {{button|x}} to {{button|c}}.
}}
{{-}}

==264: Attack Chip==
{{Card Infobox DDCB-DM
 |name=Attack Chip
 |name_jp=攻撃チップ
 |name_jp_roman=Kougeki Chip
 |number=264
 |effect=Boost own Attack Power +300.
}}
{{-}}

==265: High Speed Disk==
{{Card Infobox DDCB-DM
 |name=High Speed Disk
 |name_jp=高速プラグイン
 |name_jp_roman=Kousoku Plugin
 |number=265
 |effect=Randomly discard 1 Card from own Hand. Opponent's Attack Power is 0.
}}
{{-}}

==266: Recovery Floppy==
{{Card Infobox DDCB-DM
 |name=Recovery Floppy
 |name_jp=回復フロッピー
 |name_jp_roman=Kaifuku Floppy
 |number=266
 |effect=Recover own HP by +300.
}}
{{-}}

==267: Attack Disk {{button|c}}==
{{Card Infobox DDCB-DM
 |name=Attack Disk {{button|c}}
 |name_jp=攻撃プラグイン○
 |name_jp_roman=Kougeki Plugin ○
 |filename=Attack Disk C
 |number=267
 |effect=Own {{button|c}} Attack Power is doubled.
}}
{{-}}

==268: Attack Disk {{button|t}}==
{{Card Infobox DDCB-DM
 |name=Attack Disk {{button|t}}
 |name_jp=攻撃プラグイン△
 |name_jp_roman=Kougeki Plugin △
 |filename=Attack Disk T
 |number=268
 |effect=Own {{button|t}} Attack Power is doubled.
}}
{{-}}

==269: Attack Disk {{button|x}}==
{{Card Infobox DDCB-DM
 |name=Attack Disk {{button|x}}
 |name_jp=攻撃プラグイン×
 |name_jp_roman=Kougeki Plugin ×
 |filename=Attack Disk X
 |number=269
 |effect=Own {{button|x}} Attack Power is doubled.
}}
{{-}}

==270: Defense Disk {{button|c}}==
{{Card Infobox DDCB-DM
 |name=Defense Disk {{button|c}}
 |name_jp=防御プラグイン○
 |name_jp_roman=Bougyo Plugin ○
 |filename=Defense Disk C
 |number=270
 |effect=Opponent's {{button|c}} Attack Power is 0.
}}
{{-}}

==271: Defense Disk {{button|t}}==
{{Card Infobox DDCB-DM
 |name=Defense Disk {{button|t}}
 |name_jp=防御プラグイン△
 |name_jp_roman=Bougyo Plugin △
 |filename=Defense Disk T
 |number=271
 |effect=Opponent's {{button|t}} Attack Power is 0.
}}
{{-}}

==272: Defense Disk {{button|x}}==
{{Card Infobox DDCB-DM
 |name=Defense Disk {{button|x}}
 |name_jp=防御プラグイン×
 |name_jp_roman=Bougyo Plugin ×
 |filename=Defense Disk X
 |number=272
 |effect=Opponent's {{button|x}} Attack Power is 0.
}}
{{-}}

==273: Digi-Garnet==
{{Card Infobox DDCB-DM
 |name=Digi-Garnet
 |name_jp=デジガーネット
 |name_jp_roman=
 |number=273
 |effect=Boost own Attack Power +100.
}}
{{-}}

==274: Digi-Amethyst==
{{Card Infobox DDCB-DM
 |name=Digi-Amethyst
 |name_jp=デジアメジスト
 |name_jp_roman=
 |number=274
 |effect=Recover own HP by +100.
}}
{{-}}

==275: Digi-Aquamarine==
{{Card Infobox DDCB-DM
 |name=Digi-Aquamarine
 |name_jp=デジアクアマリン
 |name_jp_roman=
 |number=275
 |effect=KO'd Digimon revives with 100 HP. Battle is still lost.
}}
{{-}}

==276: Digi-Diamond==
{{Card Infobox DDCB-DM
 |name=Digi-Diamond
 |name_jp=デジダイヤモンド
 |name_jp_roman=
 |number=276
 |effect=Draw 2 Cards from Online Deck.
}}
{{-}}

==277: Digi-Emerald==
{{Card Infobox DDCB-DM
 |name=Digi-Emerald
 |name_jp=デジエメラルド
 |name_jp_roman=
 |number=277
 |effect=Change own Specialty to Nature.
}}
{{-}}

==278: Digi-Pearl==
{{Card Infobox DDCB-DM
 |name=Digi-Pearl
 |name_jp=デジパール
 |name_jp_roman=
 |number=278
 |effect=Changes own Specialty to Rare.
}}
{{-}}

==279: Digi-Ruby==
{{Card Infobox DDCB-DM
 |name=Digi-Ruby
 |name_jp=デジルビー
 |name_jp_roman=
 |number=279
 |effect=Changes own Specialty to Fire.
}}
{{-}}

==280: Digi-Sardnyx==
{{Card Infobox DDCB-DM
 |name=Digi-Sardnyx
 |name_jp=デジサードニクス
 |name_jp_roman=Digi-Sardonyx
 |number=280
 |effect=Change own Specialty to Darkness.
}}
{{-}}

==281: Digi-Sapphire==
{{Card Infobox DDCB-DM
 |name=Digi-Sapphire
 |name_jp=デジサファイア
 |name_jp_roman=
 |number=281
 |effect=Change own Specialty to Ice.
}}
{{-}}

==282: Digi-Opal==
{{Card Infobox DDCB-DM
 |name=Digi-Opal
 |name_jp=デジオパール
 |name_jp_roman=
 |number=282
 |effect=Own attack becomes {{button|c}}.
}}
{{-}}

==283: Digi-Topaz==
{{Card Infobox DDCB-DM
 |name=Digi-Topaz
 |name_jp=デジトパーズ
 |name_jp_roman=
 |number=283
 |effect=Own attack becomes {{button|t}}.
}}
{{-}}

==284: Digi-Turquoise==
{{Card Infobox DDCB-DM
 |name=Digi-Turquoise
 |name_jp=デジターコイズ
 |name_jp_roman=
 |number=284
 |effect=Own attack becomes {{button|x}}.
}}
{{-}}

==285: Wild Sevens==
{{Card Infobox DDCB-DM
 |name=Wild Sevens
 |name_jp=ワイルドセブンズ
 |name_jp_roman=
 |number=285
 |effect=Own Attack Power is tripled.
}}
{{-}}

==286: Holy Sevens==
{{Card Infobox DDCB-DM
 |name=Holy Sevens
 |name_jp=ホーリーセブンズ
 |name_jp_roman=
 |number=286
 |effect=Recover own HP by +1000.
}}
{{-}}

==287: Dark Sevens==
{{Card Infobox DDCB-DM
 |name=Dark Sevens
 |name_jp=ダークセブンズ
 |name_jp_roman=
 |number=287
 |effect=If opponent's HP are lower then own, opponent's HP become 10.
}}
{{-}}

==288: Grand Sevens==
{{Card Infobox DDCB-DM
 |name=Grand Sevens
 |name_jp=グランドセブンズ
 |name_jp_roman=Ground Sevens
 |number=288
 |effect=Own Attack Power is boosted by the number of own HP.
}}
{{-}}

==289: Mystic Sevens==
{{Card Infobox DDCB-DM
 |name=Mystic Sevens
 |name_jp=ミスティセブンズ
 |name_jp_roman=Misty Sevents
 |number=289
 |effect=Opponent's Support and Option Effects are voided. His Attack Power is 0.
}}
{{-}}

==290: Speed Sevens==
{{Card Infobox DDCB-DM
 |name=Speed Sevens
 |name_jp=スピードセブンズ
 |name_jp_roman=
 |number=290
 |effect=Attack first. Own attack becomes "Eat-up HP." Boost Attack Power +200.
}}
{{-}}

==291: Reverse Sevens==
{{Card Infobox DDCB-DM
 |name=Reverse Sevens
 |name_jp=リバースセブンズ
 |name_jp_roman=
 |number=291
 |effect=Move top 10 Cards from Offline Pile to Online Deck, then shuffle.
}}
{{-}}

==292: Rosemon's Lure==
{{Card Infobox DDCB-DM
 |name=Rosemon's Lure
 |name_jp=ロゼモンの誘惑
 |name_jp_roman=Rosemon no Yuuwaku
 |number=292
 |effect=Opponent discards his Hand and all Cards in his DP Slot.
}}
{{-}}

==293: Download Digivolve==
{{Card Infobox DDCB-DM
 |name=Download Digivolve
 |name_jp=ダウンローダー
 |name_jp_roman=Downloader
 |number=293
 |effect=Can digivolve regardless of own Specialty, Level, or Digivolve Pts.
}}
{{-}}

==294: ArmorCrush Digivolve==
{{Card Infobox DDCB-DM
 |name=ArmorCrush Digivolve
 |name_jp=アーマー突破
 |name_jp_roman=Armor Toppa
 |number=294
 |effect=Digivolve a Level A Digimon to C or U. (DP are needed.)
}}
{{-}}

==295: Special Digivolve==
{{Card Infobox DDCB-DM
 |name=Special Digivolve
 |name_jp=特殊進化
 |name_jp_roman=Tokushu Shinka
 |number=295
 |effect=Can digivolve regardless of own Specialty by adding DP +20.
}}
{{-}}

==296: Mutant Digivolve==
{{Card Infobox DDCB-DM
 |name=Mutant Digivolve
 |name_jp=突然変異
 |name_jp_roman=Totsuzenhen'i
 |number=296
 |effect=Can digivolve Digimon at same Level. (Need DP) (Ignore Specialty)
}}
{{-}}

==297: Warp Digivolve==
{{Card Infobox DDCB-DM
 |name=Warp Digivolve
 |name_jp=ワープ進化
 |name_jp_roman=Warp Shinka
 |number=297
 |effect=Can digivolve from R to U. (DP are needed.)
}}
{{-}}

==298: De-Armor Digivolve==
{{Card Infobox DDCB-DM
 |name=De-Armor Digivolve
 |name_jp=アーマー解除
 |name_jp_roman=Armor Kaijo
 |number=298
 |effect=Downgrade a Level A Digimon to Level R.
}}
{{-}}

==299: Speed Digivolve==
{{Card Infobox DDCB-DM
 |name=Speed Digivolve
 |name_jp=スピード進化
 |name_jp_roman=Speed Shinka
 |number=299
 |effect=Can disregard DP in digivolving. (Not possible in Abnormal states)
}}
{{-}}

==300: Digi-devolve==
{{Card Infobox DDCB-DM
 |name=Digi-devolve
 |name_jp=退化
 |name_jp_roman=Taika
 |number=300
 |effect=DownGrade own digivolution by 1 Level. HP double when successful.
}}
{{-}}
"""


def createMonsterCard(card):
    # parse the card into list of non-whitespace strings
    nw = re.split(r"\s+", card)
    # remove non-key strings
    card_filtered = list(filter(lambda x: "|" in x, nw))
    # monster card dict
    monster_card = {
        "name": "",
        "number": "",
        "level": "",
        "specialty": "",
        "hp": "",
        "dp": "",
        "pp": "",
        "c_attack": "",
        "c_pow": "",
        "t_attack": "",
        "t_pow": "",
        "x_attack": "",
        "x_pow": "",
        "x_effect": "",
        "support": "",
    }

    # loop through the target keys
    for j, key in enumerate(monster_card.keys()):
        # loop through the filtered card
        for value in card_filtered:
            key_full_name = key + "="
            # get the matching target key and value in the filtered card
            if key_full_name in value:
                # value start index
                value_start_index = value.find("=") + 1
                # value
                target_value = value[value_start_index:]
                monster_card[key] = target_value

    # map name to monster_card dict
    name = re.search(r"name=.+\n", card)
    monster_card["name"] = card[name.start() + len("name=") : name.end() - 1]
    # map level to monster_card dict
    level = re.search(r"level=.+\n", card)
    monster_card["level"] = card[level.start() + len("level=") : level.end() - 1]
    # map c_attack to monster_card dict
    c_attack = re.search(r"c_attack=.+\n", card)
    monster_card["c_attack"] = card[
        c_attack.start() + len("c_attack=") : c_attack.end() - 1
    ]
    # map t_attack to monster_card dict
    t_attack = re.search(r"t_attack=.+\n", card)
    monster_card["t_attack"] = card[
        t_attack.start() + len("t_attack=") : t_attack.end() - 1
    ]
    # map x_attack to monster_card dict
    x_attack = re.search(r"x_attack=.+\n", card)
    monster_card["x_attack"] = card[
        x_attack.start() + len("x_attack=") : x_attack.end() - 1
    ]
    # map x_effect to monster_card dict
    x_effect = re.search(r"x_effect=.+\n", card)
    monster_card["x_effect"] = card[
        x_effect.start() + len("x_effect=") : x_effect.end() - 1
    ]
    # map support to monster_card dict
    support = re.search(r"support=.+\n", card)
    monster_card["support"] = card[
        support.start() + len("support=") : support.end() - 1
    ]
    return monster_card


def createEffectCard(card):
    # effect card dict
    effect_card = {
        "name": "",
        "number": "",
        "effect": "",
    }
    # map name to monster_card dict
    name = re.search(r"name=.+\n", card)
    effect_card["name"] = card[name.start() + len("name=") : name.end() - 1]
    # map number to monster_card dict
    number = re.search(r"number=.+\n", card)
    effect_card["number"] = card[number.start() + len("number=") : number.end() - 1]
    # map effect to monster_card dict
    effect = re.search(r"effect=.+\n", card)
    effect_card["effect"] = card[effect.start() + len("effect=") : effect.end() - 1]
    return effect_card


# parse the wiki strings to list
cards_list = cards_string.split("{{-}}")
cards_list = cards_list[:-1]

# monster cards list result
monster_card_list = []
# effect cards list result
effect_card_list = []
# cards list result
cards = {"monster_cards": [], "effect_cards": []}

# loop through the cards
for i, card in enumerate(cards_list):
    # monster card
    if "level" in card:
        # map values to monster_card dict
        monster_card = createMonsterCard(card)
        # add monster card to the monster cards list
        monster_card_list.append(monster_card)
    # effect card
    else:
        # map values to effect_card dict
        effect_card = createEffectCard(card)
        # add effect card to the effect cards list
        effect_card_list.append(effect_card)

cards["monster_cards"] = monster_card_list
cards["effect_cards"] = effect_card_list

# write monster cards Python list dict to JSON file
with open("monsterCards.json", "w") as f:
    json.dump(monster_card_list, f, indent=2)
# write effect cards Python list dict to JSON file
with open("effectCards.json", "w") as f:
    json.dump(effect_card_list, f, indent=2)

# write cards master JSON file
with open("cards.json", "w") as f:
    json.dump(cards, f, indent=2)