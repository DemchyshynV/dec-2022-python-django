from django_filters import rest_framework as filters


class UserFilter(filters.FilterSet):
    email_startswith = filters.CharFilter('email', 'istartswith')
    name_startswith = filters.CharFilter('profile', 'name__istartswith')
    surname_startswith = filters.CharFilter('profile', 'surname__istartswith')

    email_contains = filters.CharFilter('email', 'icontains')
    name_contains = filters.CharFilter('profile', 'name__icontains')
    surname_contains = filters.CharFilter('profile', 'surname__icontains')

    order = filters.OrderingFilter(
        fields=(
            'id',
            'email',
            ('profile__name', 'name'),
            ('profile__surname', 'surname'),
            ('profile__age', 'age')
        )
    )
