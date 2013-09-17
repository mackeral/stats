<?
class Citation {

    var $dateCreated;
    var $datestamp;
    var $dcCreator; //dc:creator is the author and there should be multiple listings if there are multiple authors (each one on a new dc:creator field)
    var $dcDate;
    var $dcDateCreated;
    var $dcDescription;
    var $dcDescriptionAbstract;
    var $dcFormat;
    var $dcIdentifier;
    var $dcPublisher;
    var $dcSource; // dc:source is the formal name of the structure where the item is found (i.e., Faculty Scholarship is facpubs)
    var $dcSubject;
    var $dcTitle;
    var $dcType;
    var $descriptionAbstract;
    var $id;
    var $identifier;
    var $setSpec;

    function __construct(){
        $dbCite = func_get_arg(0);
    }
}
?>