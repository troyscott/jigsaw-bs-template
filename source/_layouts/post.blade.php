@extends('_layouts.master')

@section('content')
<h1>{{ $title }}</h1>
<h4>by {{ $author }}</h4>
{{ $pubDate }}
@yield('postContent')
@endsection
