REST_FRAMEWORK = {
	'DEFAULT_PAGINATION_CLASS': 'board.restconf.pagination.BoardAPIPaginator',
	'DEFAULT_FILTER_BACKENDS': (
			'rest_framework.filters.SearchFilter',
			'rest_framework.filters.OrderingFilter',
		),
	'SEARCH_PARAM': 'search',
	'ORDERING_PARAM': 'ordering',
}