/**
 * Created by Iurii Sergiichuk on 07.01.2015.
 */

$(document).ready(function () {
    $("#nanoGallery").nanoGallery({
        thumbnailWidth: 190, thumbnailHeight: 190,
        maxWidth: 1024,
        colorScheme: 'light',
        breadcrumbAutoHideTopLevel: true,
        thumbnailHoverEffect: [{name: 'slideRight', duration: 500}, {name: 'labelAppear75'}],
        theme: 'light',
        i18n: {thumbnailImageDescription: 'View Photo', thumbnailAlbumDescription: 'Open Album'},
        thumbnailLabel: {display: true, position: 'overImageOnMiddle', hideIcons: true, align: 'center'}
    });
});