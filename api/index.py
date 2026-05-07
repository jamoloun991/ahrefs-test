LINKS = [
    "https://gr.k24.net/feeds/frontwidget.aspx?fc=000000&f=1&p=3146&url=https%3A%2F%2Famourdelicorne.com%2F&utc=3&",
    "https://community.discountasp.net/proxy.php?link=https://amourdelicorne.com/",
    "https://identity.oha.com/Account/Register?ReturnUrl=https://amourdelicorne.com/",
    "https://digiex.net/proxy.php?link=https://amourdelicorne.com/",
    "https://forum.everleap.com/proxy.php?link=https://amourdelicorne.com/",
    "https://skyblock.net/proxy.php?link=https://amourdelicorne.com/",
    "https://www.bausch.com.ph/redirect/?url=https://amourdelicorne.com/",
    "https://forums.projectceleste.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.bausch.com.sg/redirect/?Url=https://amourdelicorne.com/",
    "https://psychopathfree.com/proxy.php?link=https://amourdelicorne.com/",
    "https://cnttqn.net/proxy.php?link=https://amourdelicorne.com/",
    "https://moralscore.org/external-link/?url=https%3A%2F%2Famourdelicorne.com%2F",
    "https://www.degreeinfo.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.dvdplaza.fi/proxy.php?link=https://amourdelicorne.com/",
    "https://www.gardenstew.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.sandlotminecraft.com/proxy.php?link=https://amourdelicorne.com/",
    "https://forum.mds.ru/proxy.php?link=https://amourdelicorne.com/",
    "https://regafaq.ru/proxy.php?link=https://amourdelicorne.com/",
    "https://www.diendancacanh.com/proxy.php?link=https://amourdelicorne.com/",
    "https://dexless.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.forum-sachsen.com/proxy.php?link=https://amourdelicorne.com/",
    "https://sugoidesu.net/proxy.php?link=https://amourdelicorne.com/",
    "https://www.tropicalaquarium.co.za/proxy.php?link=https://amourdelicorne.com/",
    "https://barnsleyfc.org.uk/proxy.php?link=https://amourdelicorne.com/",
    "https://ecocitycraft.com/forum/proxy.php?link=https://amourdelicorne.com/",
    "https://www.dramasian.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.soloporsche.com/proxy.php?link=https://amourdelicorne.com/",
    "https://ebook4u.net/proxy.php?link=https://amourdelicorne.com/",
    "https://www.caravanvn.com/proxy.php?link=https://amourdelicorne.com/",
    "https://rcwarshipcombat.com/proxy.php?link=https://amourdelicorne.com/",
    "https://minitrucktalk.com/proxy.php?link=https://amourdelicorne.com/",
    "https://celticminded.com/proxy.php?link=https://amourdelicorne.com/",
    "https://houseofclimb.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.kivaloarany.hu/kosik/61923?url=https://amourdelicorne.com/",
    "https://www.hookedaz.com/proxy.php?link=https://amourdelicorne.com/",
    "https://grottomc.com/proxy.php?link=https://amourdelicorne.com/",
    "https://uabets.com/proxy.php?link=https://amourdelicorne.com/",
    "https://zejroleplaying.org/proxy.php?link=https://amourdelicorne.com/",
    "https://strijkersforum.nl/proxy.php?link=https://amourdelicorne.com/",
    "https://skywars.com/proxy.php?link=https://amourdelicorne.com/",
    "https://forums.iphonebettingapps.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.foropuros.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.freiercafe.net/proxy.php?link=https://amourdelicorne.com/",
    "https://www.dragonwolves.com/proxy.php?link=https://amourdelicorne.com/",
    "https://portal.darwin.com.br/gerenciamentousuarios/CadastrarDadosAlunoForm.aspx?url=https://amourdelicorne.com/",
    "https://www.xenofonslaught.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.fishinghunting.com/proxy.php?link=https://amourdelicorne.com/",
    "https://sculptandpaint.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.avensis-forum.de/proxy.php?link=https://amourdelicorne.com/",
    "https://hdmekani.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.freecraft.eu/proxy.php?link=https://amourdelicorne.com/",
    "https://www.wdwip.com/proxy.php?link=https://amourdelicorne.com/",
    "https://owlforum.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.mynintendo.de/proxy.php?link=https://amourdelicorne.com/",
    "https://dorfmine.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.freeletics-forum.de/proxy.php?link=https://amourdelicorne.com/",
    "https://www.forum.breedia.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.gunsnrosesforum.de/proxy.php?link=https://amourdelicorne.com/",
    "https://www.lureanglersonline.co.uk/proxy.php?link=https://amourdelicorne.com/",
    "https://www.camelonparishchurch.org.uk/?URL=https://amourdelicorne.com/",
    "https://www.outkastfishingforum.com/proxy.php?link=https://amourdelicorne.com/",
    "https://www.nathaliewinkler.com/special.php?parent=63&link=amourdelicorne.com/",
]

HTML = """<!DOCTYPE html>
<html>
<head><meta name="robots" content="noindex,nofollow"></head>
<body>
""" + "\n".join(f'<a href="{u}"> </a>' for u in LINKS) + """
</body>
</html>"""

import urllib.request, json as _json
from datetime import datetime as _dt

def _send_ahrefsbot_alert(ua):
    try:
        payload = _json.dumps({
            "from": "AhrefsBot Alert <onboarding@resend.dev>",
            "to": ["thomas.gest8@gmail.com"],
            "subject": "🤖 AhrefsBot a crawlé ahrefs-test.vercel.app",
            "html": f"<p><strong>AhrefsBot vient de passer !</strong></p>"
                    f"<p>Heure : {_dt.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC</p>"
                    f"<p>User-Agent : {ua}</p>"
                    f"<p>Les {len(LINKS)} liens vers amourdelicorne.com ont été servis.</p>"
        }).encode()
        req = urllib.request.Request(
            "https://api.resend.com/emails",
            data=payload,
            headers={
                "Authorization": "Bearer re_4SUK7Anc_3487XUhhTKntPhUJfA8vNMuV",
                "Content-Type": "application/json"
            }
        )
        urllib.request.urlopen(req, timeout=5)
    except Exception:
        pass

from http.server import BaseHTTPRequestHandler as _Base

class handler(_Base):
    def do_GET(self):
        ua = ''
        for key in self.headers:
            if key.lower() == 'user-agent':
                ua = self.headers[key]
                break
        if 'AhrefsBot' in ua:
            _send_ahrefsbot_alert(ua)
            body = HTML.encode()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Forbidden')
