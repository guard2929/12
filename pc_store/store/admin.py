from django.contrib import admin
from .models import CPU, GPU, RAM, Storage, PCBuild, Product, PrebuiltOrder


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'has_image')
    search_fields = ('name',)
    list_filter = ('price',)

    def has_image(self, obj):
        return bool(obj.image)

    has_image.boolean = True
    has_image.short_description = 'Изображение'


@admin.register(PCBuild)
class PCBuildAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_ordered', 'order_status', 'created_at')
    list_filter = ('is_ordered', 'order_status', 'created_at')
    search_fields = ('user__username',)
    filter_horizontal = ('cpu', 'gpu', 'ram', 'storage')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    fieldsets = (
        ('Пользователь и статус', {
            'fields': ('user', 'is_ordered', 'order_status')
        }),
        ('Комплектующие', {
            'fields': ('cpu', 'gpu', 'ram', 'storage')
        }),
        ('Даты', {
            'fields': ('created_at',),
        }),
    )
    readonly_fields = ('created_at',)


@admin.register(PrebuiltOrder)
class PrebuiltOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'product__name')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


@admin.register(CPU)
class CPUAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_image')
    search_fields = ('name',)

    def has_image(self, obj):
        return bool(obj.image)

    has_image.boolean = True
    has_image.short_description = 'Изображение'


@admin.register(GPU)
class GPUAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_image')
    search_fields = ('name',)

    def has_image(self, obj):
        return bool(obj.image)

    has_image.boolean = True
    has_image.short_description = 'Изображение'


@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_image')
    search_fields = ('name',)

    def has_image(self, obj):
        return bool(obj.image)

    has_image.boolean = True
    has_image.short_description = 'Изображение'


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_image')
    search_fields = ('name',)

    def has_image(self, obj):
        return bool(obj.image)

    has_image.boolean = True
    has_image.short_description = 'Изображение'
