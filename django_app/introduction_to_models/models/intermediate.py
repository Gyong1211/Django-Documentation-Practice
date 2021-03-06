from django.db.models import Q
from django.utils import timezone

from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    @property
    def current_club(self):
        # 해당 선수의 가입 일자가 현재 시간보다 이전이면서,
        # 탈퇴한 기록이 없는 팀(1개의 팀이 선택될 것이다.)의
        # 이름을 반환한다.
        return self.club_set.get(
            # tradeinfo__date_joined__lte=timezone.now(), # <-없어도 됨
            # tradeinfo__date_leaved=None # Python 문법
            tradeinfo__date_leaved__isnull = True, # DB에서 해당 값이 Null인지 판단
        )

    @property
    def current_tradeinfo(self):
        # 현재 선수가 뛰고있는 팀은 1군데기 때문에 filter대신 get을 사용한다.
        # 가입일자가 현재보다 전이고, 탈퇴한 기록이 없는 TradeInfo 쿼리를 긁어온다.
        # self.current_tradeinfo 뒤에 .player나 .club, .date_
        return TradeInfo.objects.get(
            player__id=self.id,
            # date_joined__lte=timezone.now(), #<-없어도됨
            # date_leaved=None, # Python 문법
            date_leaved__isnull = True, # DB에서 해당 값이 Null인지 판단
        )



class Club(models.Model):
    name = models.CharField(max_length=40)
    players = models.ManyToManyField(
        Player,
        through='TradeInfo',
        through_fields=('club', 'player'),
    )

    def __str__(self):
        return self.name

    def squad(self, year=None):
        if year is None:
            # 연도를 입력하지 않으면, 현재 일 기준으로 이전에 가입하고,
            # 탈퇴한 기록이 없는 선수들의 name을 리스트로 반환한다.
            # return [club_squad.player.name for club_squad in
            #         TradeInfo.objects.filter(
            #             club__id=self.id,
            #             date_joined__lte=timezone.now(),
            #             date_leaved=None,
            #         )]

            return self.player.filter(tradeinfo_set__date_leaved__isnull=True)

        else:
            # 연도를 입력하면, 해당 년 1월 1일 이전에 가입했고,
            # 해당 년 12월 31일 이후에 탈퇴하거나 탈퇴하지 않은 선수들의 쿼리셋을 반환한다.
            return self.player.filter(
                Q(date_joined__lt=timezone.datetime(year+1, 1, 1)) &
                (Q(date_leaved__gt=timezone.datetime(year, 1, 1)) | Q(date_leaved__isnull=True)))


class TradeInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    date_joined = models.DateField()
    date_leaved = models.DateField(null=True, blank=True, )
    recommender = models.ForeignKey(
        Player,
        on_delete=models.PROTECT,
        related_name="tradeinfo_set_by_recommender",
        null=True,
        blank=True
    )
    prev_club = models.ForeignKey(
        Club,
        on_delete=models.PROTECT,
        related_name="+",
        null=True,
        blank=True
    )

    def __str__(self):
        return '{}, {} ({} ~ {})'.format(
            self.player.name,
            self.club.name,
            self.date_joined,
            #self.date_leaved if self.date_leaved else '현직',
            self.date_leaved or '현직',
        )

    @property
    def is_current(self):
        return self.date_leaved is None


