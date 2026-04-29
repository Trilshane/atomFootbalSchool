from django.contrib import admin

from .models import Player, Position, Year


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("get_display_name", "get_position", "get_year")
    list_filter = ("position", "year")
    search_fields = ("first_name", "last_name")

    @admin.display(description="Имя", ordering="last_name")
    def get_display_name(self, obj):
        first = obj.first_name
        last = obj.last_name
        full = f"{first} {last}".strip()
        return full

    @admin.display(description="Позиция")
    def get_position(self, obj):
        positions = obj.position.all()
        if not positions:
            return "—"
        return ", ".join(p.position_short_name for p in positions)
    
    @admin.display(description="Год")
    def get_year(self, obj):
        years = obj.year.all()
        return ", ".join(str(y) for y in years) or "—"


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("position_name",)
    list_filter = ("position_short_name",)


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ("year",)
    list_filter = ("year",)
