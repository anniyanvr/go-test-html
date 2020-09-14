import groovy.json.JsonSlurper
import groovy.text.SimpleTemplateEngine
new File("/var/lib/jenkins/workspace/test-pipeline/go-test-html/Tflint-resourcegroups.html").withWriter("UTF-8"){writer->
    new SimpleTemplateEngine()
        .createTemplate( new File("/var/lib/jenkins/workspace/test-pipeline/go-test-html/tflint.gsp") )
        .make( data:new JsonSlurper().parse(new File("/var/lib/jenkins/workspace/test-pipeline/dsp-terratest/Tflint_resourcegroups.json")) )
        .writeTo( writer )
}
