$(document).ready(function () {

    $('#usuarios').DataTable({
        "language": {
            "lengthMenu": "Mostrar _MENU_ usuarios",
            "zeroRecords": "No se encontraron resultados",
            "info": "Mostrando usuarios del _START_ al _END_ de un total de _TOTAL_ registros",
            "infoEmpty": "No existen usuarios",
            "infoFiltered": "(filtrado de un total de _MAX_ usuarios",
            "sSearch": "Buscar:",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Ultimo",
                "sNext": "Siguiente",
                "sPrevious": "Anterior",
            },
            "sProcessing": "Procesando..."
        },
        dom: 'lifBtp',
        "pageLength": 50,
        "lengthMenu":	[[5, 10, 20, 25, 50, -1], [5, 10, 20, 25, 50, "Todos"]],
        "order": [[ 2, "asc" ]], 
        
    }); //Fin de Usuarios  Datatable
    $('#usuarios').cardtable();

    $('#reportes').DataTable({
        "language": {
            "lengthMenu": "Mostrar _MENU_ usuarios",
            "zeroRecords": "No se encontraron resultados",
            "info": "Mostrando usuarios del _START_ al _END_ de un total de _TOTAL_ registros",
            "infoEmpty": "No existen usuarios",
            "infoFiltered": "(filtrado de un total de _MAX_ usuarios",
            "sSearch": "Buscar:",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Ultimo",
                "sNext": "Siguiente",
                "sPrevious": "Anterior",
            },
            "sProcessing": "Procesando..."
        },
        dom: 'lifBtp',
        "pageLength": 20,
        "lengthMenu":	[[5, 10, 20, 25, 50, -1], [5, 10, 20, 25, 50, "Todos"]],
        "order": [[ 0, "asc" ]], 

    }); // Fin Reportes DataTable
    $('#reportes').cardtable();


    $('#biblioteca-personal').DataTable({
        "language": {
            "lengthMenu": "Mostrar _MENU_ entradas",
            "zeroRecords": "Su biblioteca esta vacia",
            "info": "Mostrando entradas del _START_ al _END_ de un total de _TOTAL_ registros",
            "infoEmpty": "Sin resultados",
            "infoFiltered": "(filtrado de un total de _MAX_ entradas",
            "sSearch": "Buscar:",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Ultimo",
                "sNext": "Siguiente",
                "sPrevious": "Anterior",
            },
            "sProcessing": "Procesando..."
        },
        dom: 'lifBtp',
        "pageLength": 20,
        "lengthMenu":	[[5, 10, 20, 25, 50, -1], [5, 10, 20, 25, 50, "Todos"]],
        "order": [[ 0, "desc" ]], 
    }); //Fin Biblioteca personal Data Table
    $('#biblioteca-personal').cardtable();
    
//Configuracion Table-Publicaciones
    $('#publicaciones').DataTable({
        "language": {
            "lengthMenu": "Mostrar _MENU_ entradas",
            "zeroRecords": "No se encontraron resultados",
            "info": "Mostrando entradas del _START_ al _END_ de un total de _TOTAL_ entradas",
            "infoEmpty": "Sin resultados",
            "infoFiltered": "(filtrado de un total de _MAX_ entradas)",
            "sSearch": "Buscar:",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Ultimo",
                "sNext": "Siguiente",
                "sPrevious": "Anterior",
            },
            "sProcessing": "Procesando..."
        },
        dom: 'li<"toolbar">fBtp',
        "pageLength": 50,
        "lengthMenu":	[[5, 10, 20, 25, 50, -1], [5, 10, 20, 25, 50, "Todos"]],
        "order": [[ 2, "desc" ]],    
    }); 
    $("div.toolbar").html('<small>Favor de seleccionar los artículos para agregar a su biblioteca</small>');
    $('#publicaciones').cardtable();
//Fin Publicaciones

    $('#reportesEnviados').DataTable({
        "language": {
            "lengthMenu": "Mostrar _MENU_ reportes",
            "zeroRecords": "No se encontraron resultados",
            "info": "Mostrando reportes del _START_ al _END_ de un total de _TOTAL_ registros",
            "infoEmpty": "No existen reportes enviados",
            "infoFiltered": "(filtrado de un total de _MAX_ registros",
            "sSearch": "Buscar:",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Ultimo",
                "sNext": "Siguiente",
                "sPrevious": "Anterior",
            },
            "sProcessing": "Procesando..."
        },
        dom: 'lifBtp',
        "pageLength": 50,
        "lengthMenu":	[[5, 10, 20, 25, 50, -1], [5, 10, 20, 25, 50, "Todos"]],
        "order": [[ 1, "desc" ]],  
    }); //Fin de Usuarios  Datatable
    $('#reportesEnviados').cardtable();


//Scrips de CRUD
    $(".alert-success").fadeTo(2000, 500).slideUp(500, function(){ $(".alert-dismissible").alert('close'); });
    $(".alert-primary").fadeTo(2000, 500).slideUp(500, function(){ $(".alert-dismissible").alert('close'); });             
    $(".alert-danger").fadeTo(2000, 500).slideUp(500, function(){ $(".alert-dismissible").alert('close'); });     
});
