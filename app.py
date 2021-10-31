from flask import Flask,render_template




app=Flask(__name__,template_folder='templates')
app.secret_key = 'elementdekho'

@app.route("/")
def homepage():
	return render_template("home.html")


@app.route("/element/h")
def hydrogen():
	return render_template("hydrogen.html")



@app.route("/element/he")
def helium():
	return render_template("helium.html")



@app.route("/element/li")
def lithium():
	return render_template("lithium.html")


@app.route("/element/be")
def beryllium():
	return render_template("beryllium.html")	



@app.route("/element/b")
def boron():
	return render_template("boron.html")	



@app.route("/element/c")
def carbon():
	return render_template("carbon.html")	


@app.route("/element/n")
def nitrogen():
	return render_template("nitrogen.html")


@app.route("/element/o")
def oxygen():
	return render_template("oxygen.html")


@app.route("/element/f")
def fluorine():
	return render_template("fluorine.html")


@app.route("/element/ne")
def neon():
	return render_template("neon.html")


@app.route("/element/na")
def sodium():
	return render_template("sodium.html")


@app.route("/element/mg")
def magnesium():
	return render_template("magnesium.html")


@app.route("/element/al")
def aluminium():
	return render_template("aluminium.html")


@app.route("/element/si")
def silicon():
	return render_template("silicon.html")


@app.route("/element/p")
def phosphorus():
	return render_template("phosphorus.html")


@app.route("/element/s")
def sulfur():
	return render_template("sulfur.html")



@app.route("/element/cl")
def chlorine():
	return render_template("chlorine.html")


@app.route("/element/ar")
def argon():
	return render_template("argon.html")


@app.route("/element/k")
def potassium():
	return render_template("potassium.html")


@app.route("/element/ca")
def calcium():
	return render_template("calcium.html")


@app.route("/element/sc")
def scandium():
	return render_template("scandium.html")


@app.route("/element/ti")
def titanium():
	return render_template("titanium.html")


@app.route("/element/v")
def vanadium():
	return render_template("vanadium.html")


@app.route("/element/cr")
def chromium():
	return render_template("chromium.html")


@app.route("/element/mn")
def manganese():
	return render_template("manganese.html")


@app.route("/element/fe")
def iron():
	return render_template("iron.html")


@app.route("/element/co")
def cobalt():
	return render_template("cobalt.html")


@app.route("/element/ni")
def nickel():
	return render_template("nickel.html")


@app.route("/element/cu")
def copper():
	return render_template("copper.html")


@app.route("/element/zn")
def zinc():
	return render_template("zinc.html")


@app.route("/element/ga")
def gallium():
	return render_template("gallium.html")


@app.route("/element/ge")
def germanium():
	return render_template("germanium.html")


@app.route("/element/as")
def arsenic():
	return render_template("arsenic.html")



@app.route("/element/se")
def selenium():
	return render_template("selenium.html")


@app.route("/element/br")
def bromine():
	return render_template("bromine.html")


@app.route("/element/kr")
def krypton():
	return render_template("krypton.html")



@app.route("/element/rb")
def rubidium():
	return render_template("rubidium.html")



@app.route("/element/sr")
def strontium():
	return render_template("strontium.html")



@app.route("/element/y")
def yttrium():
	return render_template("yttrium.html")



@app.route("/element/zr")
def zirconium():
	return render_template("zirconium.html")


@app.route("/element/nb")
def niobium():
	return render_template("niobium.html")



@app.route("/element/mo")
def molybdenum():
	return render_template("molybdenum.html")


@app.route("/element/tc")
def technetium():
	return render_template("technetium.html")


@app.route("/element/ru")
def ruthenium():
	return render_template("ruthenium.html")


@app.route("/element/rh")
def rhodium():
	return render_template("rhodium.html")



@app.route("/element/pd")
def palladium():
	return render_template("palladium.html")



@app.route("/element/ag")
def silver():
	return render_template("silver.html")


@app.route("/element/cd")
def cadmium():
	return render_template("cadmium.html")


@app.route("/element/in")
def indium():
	return render_template("indium.html")


@app.route("/element/sn")
def tin():
	return render_template("tin.html")


@app.route("/element/sb")
def antimony():
	return render_template("antimony.html")



@app.route("/element/te")
def tellurium():
	return render_template("tellurium.html")



@app.route("/element/i")
def iodine():
	return render_template("iodine.html")



@app.route("/element/xe")
def xenon():
	return render_template("xenon.html")


@app.route("/element/cs")
def caesium():
	return render_template("caesium.html")



@app.route("/element/ba")
def barium():
	return render_template("barium.html")



@app.route("/element/la")
def lanthanum():
	return render_template("lanthanum.html")



@app.route("/element/ce")
def cerium():
	return render_template("cerium.html")



@app.route("/element/pr")
def praseodymium():
	return render_template("praseodymium.html")



@app.route("/element/nd")
def neodymium():
	return render_template("neodymium.html")


@app.route("/element/pm")
def promethium():
	return render_template("promethium.html")



@app.route("/element/sm")
def samarium():
	return render_template("samarium.html")



@app.route("/element/eu")
def europium():
	return render_template("europium.html")



@app.route("/element/gd")
def gadolinium():
	return render_template("gadolinium.html")


@app.route("/element/tb")
def terbium():
	return render_template("terbium.html")


@app.route("/element/dy")
def dysprosium():
	return render_template("dysprosium.html")


@app.route("/element/ho")
def holmium():
	return render_template("holmium.html")


@app.route("/element/er")
def erbium():
	return render_template("erbium.html")



@app.route("/element/tm")
def thulium():
	return render_template("thulium.html")



@app.route("/element/yb")
def ytterbium():
	return render_template("ytterbium.html")



@app.route("/element/lu")
def lutetium():
	return render_template("lutetium.html")


@app.route("/element/hf")
def hafnium():
	return render_template("hafnium.html")



@app.route("/element/ta")
def tantalum():
	return render_template("tantalum.html")



@app.route("/element/w")
def tungsten():
	return render_template("tungsten.html")



@app.route("/element/re")
def rhenium():
	return render_template("rhenium.html")



@app.route("/element/os")
def osmium():
	return render_template("osmium.html")



@app.route("/element/ir")
def iridium():
	return render_template("iridium.html")



@app.route("/element/pt")
def platinum():
	return render_template("platinum.html")



@app.route("/element/au")
def gold():
	return render_template("gold.html")


@app.route("/element/hg")
def mercury():
	return render_template("mercury.html")



@app.route("/element/tl")
def thallium():
	return render_template("thallium.html")


@app.route("/element/pb")
def lead():
	return render_template("lead.html")



@app.route("/element/bi")
def bismuth():
	return render_template("bismuth.html")



@app.route("/element/po")
def polonium():
	return render_template("polonium.html")



@app.route("/element/at")
def astatine():
	return render_template("astatine.html")



@app.route("/element/rn")
def radon():
	return render_template("radon.html")



@app.route("/element/fr")
def francium():
	return render_template("francium.html")



@app.route("/element/ra")
def radium():
	return render_template("radium.html")



@app.route("/element/ac")
def actinium():
	return render_template("actinium.html")



@app.route("/element/th")
def thorium():
	return render_template("thorium.html")



@app.route("/element/pa")
def protactinium():
	return render_template("protactinium.html")



@app.route("/element/u")
def uranium():
	return render_template("uranium.html")



@app.route("/element/np")
def neptunium():
	return render_template("neptunium.html")



@app.route("/element/pu")
def plutonium():
	return render_template("plutonium.html")



@app.route("/element/am")
def americium():
	return render_template("americium.html")



@app.route("/element/cm")
def curium():
	return render_template("curium.html")



@app.route("/element/bk")
def berkelium():
	return render_template("berkelium.html")



@app.route("/element/cf")
def californium():
	return render_template("californium.html")



@app.route("/element/es")
def einsteinium():
	return render_template("einsteinium.html")



@app.route("/element/fm")
def fermium():
	return render_template("fermium.html")



@app.route("/element/md")
def mendelevium():
	return render_template("mendelevium.html")




@app.route("/element/no")
def nobelium():
	return render_template("nobelium.html")



@app.route("/element/lr")
def lawrencium():
	return render_template("lawrencium.html")




@app.route("/element/rf")
def rutherfordium():
	return render_template("rutherfordium.html")




@app.route("/element/db")
def dubnium():
	return render_template("dubnium.html")




@app.route("/element/sg")
def seaborgium():
	return render_template("seaborgium.html")



@app.route("/element/bh")
def bohrium():
	return render_template("bohrium.html")



@app.route("/element/hs")
def hassium():
	return render_template("hassium.html")



@app.route("/element/mt")
def meitnerium():
	return render_template("meitnerium.html")



@app.route("/element/ds")
def darmstadtium():
	return render_template("darmstadtium.html")



@app.route("/element/rg")
def roentgenium():
	return render_template("roentgenium.html")



@app.route("/element/cn")
def copernicium():
	return render_template("copernicium.html")



@app.route("/element/nh")
def nihonium():
	return render_template("nihonium.html")



@app.route("/element/fl")
def flerovium():
	return render_template("flerovium.html")



@app.route("/element/mc")
def moscovium():
	return render_template("moscovium.html")



@app.route("/element/lv")
def livermorium():
	return render_template("livermorium.html")



@app.route("/element/ts")
def tennessine():
	return render_template("tennessine.html")



@app.route("/element/og")
def oganesson():
	return render_template("oganesson.html")







if __name__ == "__main__":
    app.run(debug=True) 
