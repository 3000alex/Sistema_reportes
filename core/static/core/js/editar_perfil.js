$(document).ready(function () {
    
    $("#informacionPersonal-btn").click(function(){
        $("#nombreP").prop("disabled", false );
        $("#apellidosP").prop("disabled", false );
        $("#correoP").prop("disabled", false );
        $("#infoPersonal-btn").prop("disabled",false);
        $(this).prop("disabled",true);
    });

    $("#infoPersonal-btn").click(function(){
        $("#nombreP").prop("disabled", true );
        $("#apellidosP").prop("disabled", true );
        $("#correoP").prop("disabled", true );
        $("#infoPersonal-btn").prop("disabled",true);
        $(this).prop("disabled",true);
    });

    $("#informacionAcademica-btn").click(function(){
        $("#categoria").prop("disabled", false );
        $("#nivel_sni").prop("disabled", false );
        $("#orc_id").prop("disabled", false );
        $("#arxiv_id").prop("disabled", false );
        $("#infoAcademica-btn").prop("disabled",false);
        $(this).prop("disabled",true);
    });

    $("#infoAcademica-btn").click(function(){
        $("#categoria").prop("disabled", true );
        $("#nivel_sni").prop("disabled", true );
        $("#orc_id").prop("disabled", true );
        $("#arxiv_id").prop("disabled", true );
        $("#infoAcademica-btn").prop("disabled", true);
        $(this).prop("disabled",true);
    });

    $("#editarPerfilAdm").click(function(){
        $('#correoAlternativo').prop('disabled',false);
        $('#guardar').prop('disabled',false);
        $(this).prop("disabled",true);
    });

    $("#guardar").click(function(){
        $('#correoAlternativo').prop('disabled',true);
        $('#editarPerfilAdm').prop('disabled',false);
        $(this).prop("disabled",true);
    });
});