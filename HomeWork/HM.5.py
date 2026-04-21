class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"

    def earn(self):
        return "Заработал 500 донатов за 2 часа"


class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
        return "Набрал 3 миллиона просмотров за сутки!"


class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."

    def superpower(self):
        return "Летаю и стреляю лазерами из глаз"

class GlowStremer(Streamer, Mutant):
    def ultimate_content(self):
        return self.live() + "+" + self.superpower()

class ViralCyborg(TikToker, Mutant):
    def ultimate_content(self):
        return self.live() + "+" + self.superpower()

class DonaCyborg(Streamer, TikToker):
    def ultimate_content(self):
        return self.live() + "+" + self.earn()


g = GlowStremer()
v = ViralCyborg()
d = DonaCyborg()

print("GlowStremer MRO: ", GlowStremer.mro())
print("ViralCyborg MRO: ", ViralCyborg.mro())
print("DonaCyborg MRO: ", DonaCyborg.mro())

print("\n--- live ---")
print(g.live())
print(v.live())
print(d.live())

print("\n--- ultimate_content ---")
print(g.ultimate_content())
print(v.ultimate_content())
print(d.ultimate_content())