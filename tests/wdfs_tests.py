import wdfs
import requests
import httpretty
from sure import expect

class TestWdfsClient(object):
  def setup(self):
    params = {
       u"host":'hostname'
     , u"port": 1234
     , u"user": u'username'
    }
    self.params = params
    self.base_url = u"http://%(host)s:%(port)s/webhdfs/v1" % self.params
    self.client = wdfs.client( **params )

  @httpretty.activate
  def test_home_folder(self):

    httpretty.register_uri( httpretty.GET, self.base_url,
            body=r'{"Path": "/user/%(user)s"}' % self.params)

    home_folder = self.client.get_home_folder()
    expect( home_folder ).to.equal( u'/user/%(user)s' % self.params )

    expect( httpretty.last_request() ).to.have.property( 'querystring' ).being.equal({
        u'user.name': [ self.params['user'] ]
      , u'op':        [ u'GETHOMEDIRECTORY' ]
    })
