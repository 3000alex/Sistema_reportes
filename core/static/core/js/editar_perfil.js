$(document).ready(function () {
    
    $("#informacionPersonal").click(function(){
        $("#nombreP").prop("disabled", false );
        $("#apellidosP").prop("disabled", false );
        $("#correoP").prop("disabled", false );
        $("#guardarPerfil").prop("disabled",false);
        $(this).prop("disabled",true);
    });

    $("#informacionAcademica").click(function(){
        $("#categoria").prop("disabled", false );
        $("#nivel_sni").prop("disabled", false );
        $("#orc_id").prop("disabled", false );
        $("#arxiv_id").prop("disabled", false );
        $("#guardarPerfil").prop("disabled",false);
        $(this).prop("disabled",true);
    });

    $("#guardarPerfil").click( () => {
        $("#nombreP").prop("disabled", true);
        $("#apellidosP").prop("disabled", true );
        $("#correoP").prop("disabled", true );
        $("#guardarPerfil").prop("disabled",true);
        $("#categoria").prop("disabled", true );
        $("#nivel_sni").prop("disabled", true );
        $("#orc_id").prop("disabled", true );
        $("#arxiv_id").prop("disabled", true );
        $("#informacionAcademica").prop("disabled",false);
        $("#informacionPersonal").prop("disabled",false);
        $(this).prop("disabled",true);
    })

    $("#editarPerfilAdm").click(function(){
        $('#id_correoAlternativo').prop('disabled',false);
        $(this).prop("disabled",true);
    });
});